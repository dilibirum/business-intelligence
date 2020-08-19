# Ренднер главной страницы - лендинга
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing_page(request):
    return HttpResponse('<h1>Здесь будет лендинг о продукте</h1>')
