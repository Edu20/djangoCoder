from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def home(request):
    bienvenido = "Bienvenidos al sitio"
    pagina_html = HttpResponse(bienvenido)
    return pagina_html


def saludar(request):
    saludo = "Hola quiero saludar"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola quiero saludar, fecha:{hoy.day}/{hoy.month}/{hoy.year} "
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html

def saludar_con_html(request):
    contexto = {}
    http_responde = render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto
    )
    return http_responde
