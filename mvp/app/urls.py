from django.urls import path
from .views import main_view, account, data, dashbords


urlpatterns = [
    path('', main_view),
    path('data/', data),
    path('dashbords/', dashbords),
    path('account/', account),
]
