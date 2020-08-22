from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from .views import main_view, account, data, dashbords


urlpatterns = [
    path('', main_view),
    path('data/', data),
    path('dashbords/', dashbords),
    path('account/', account),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/logo_light.png', permanent=True)),
]
