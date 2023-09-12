from django.shortcuts import render

# Create your views here.
def render_main(request):
    context = {
        'appname': 'CakeStock',
        'name': 'Lucinda Laurent',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)