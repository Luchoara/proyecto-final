from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Posteo(models.Model):
    titulo = models.CharField(max_length=90)
    subtitulo = models.CharField(max_length=90)
    texto = models.CharField(max_length=254)
    nombre= models.CharField(max_length=90)
    email= models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f'titulo: {self.titulo}, subtitulo: {self.subtitulo}, texto: {self.texto}, nombre: {self.nombre}, email: {self.email}, fecha :{self.fecha}')

class PosteoList(models.Model):
    titulo = models.CharField(max_length=90)
    subtitulo = models.CharField(max_length=90)
    texto = models.CharField(max_length=254)
    nombre= models.CharField(max_length=90)
    email= models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
class Avatar(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

