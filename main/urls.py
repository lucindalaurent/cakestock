from django.urls import path
from main.views import render_main

app_name = 'main'

urlpatterns = [
    path('', render_main, name='render_main'),
]