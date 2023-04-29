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


def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre":"Python", "comisión": "40440"},
            {"nombre":"Frontend", "comisión": "1000"},
            {"nombre":"Diseño", "comisión": "1001"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/listaCursos.html',
        context=contexto
    )
    return http_responde