from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre":"Emanuel", "apellido": "Dautel"},
            {"nombre":"Eduardo", "apellido": "Aguirre"},
            {"nombre":"Carla", "apellido": "Conte"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/listaEstudiantes.html',
        context=contexto
    )
    return http_responde