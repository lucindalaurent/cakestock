from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.
@login_required(login_url='/login')
def render_main(request):
    if 'last_login' not in request.COOKIES.keys():
        return redirect('main:login')
    items = Item.objects.filter(user=request.user)
    context = {
        'appname': 'CakeStock',
        'name': request.user.username,
        'class': 'local user',
        'items': items,
        'last_login': request.COOKIES['last_login']
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:render_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

@csrf_exempt
def increase_amount(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(id= item_id)
        item.amount += 1
        item.save()
        return HttpResponse(b"OK", status=200)
    

@csrf_exempt
def decrease_amount(request, item_id):
    if request.method == 'POST':
        item = Item.objects.get(id= item_id)
        if item.amount > 0:
            item.amount -= 1
        item.save()
        return HttpResponse(b"OK", status=200)

@csrf_exempt
def remove_item_ajax(request, item_id):
    item = Item.objects.get(id = item_id)

    if request.method == "DELETE":
        item.delete()
        return HttpResponse(b"OK", status=200)
   

@login_required(login_url='/login')
def remove_item(request, item_id):
    item = Item.objects.get(id = item_id)

    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect(reverse('main:render_main'))
        
    context = {'item':item}
    return render(request, 'remove_item.html', context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

#pastikan hanya item milik user yang ditampilkan
def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:render_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response