from django.test import TestCase
from django.http import HttpResponse


# Create your tests here.
def interface_test(request):
    return HttpResponse('<h1>Тестирование подключения</h1>')
