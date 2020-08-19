# Ренднер главной страницы - лендинга
from django.shortcuts import render
from django.http import HttpResponse
from _datetime import datetime


# Create your views here.
def landing_page(request):
    dt = datetime.now()
    return render(request, 'mvp/landing-page.html', context={'now': dt})
