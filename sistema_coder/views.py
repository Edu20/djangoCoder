from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from django.urls import path


def saludar(request):
    saludo = "Hola quiero saludar"
    pagina_html = HttpResponse(saludo)
    return pagina_html


urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludar),
]