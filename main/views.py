from django.shortcuts import render

# Create your views here.
def render_main(request):
    context = {
        'name': 'Cheesecake',
        'desc': 'A dessert consisting of a thick, creamy filling of cheese, eggs, and sugar over a thinner crust and topped with sweet or sometimes salty items.'
    }

    return render(request, "main.html", context)