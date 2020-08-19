from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def main_view(request):
    return HttpResponse('<h1>Здесь будет главная страница приложения</h1>')


def account(request):
    return HttpResponse('<h1>Здесь будет страница аккаунта</h1>')


def data(request):
    return HttpResponse('<h1>Здесь будет страница с данными</h1>')


def dashbords(request):
    return HttpResponse('<h1>Здесь будет страница с дашбордами</h1>')
