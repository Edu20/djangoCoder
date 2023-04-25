from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=164)
    comision = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=128)
    bio = models.TextField()

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)
