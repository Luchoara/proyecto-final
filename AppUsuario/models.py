from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

## POSTEOS ##

## Posts ##
class Posteo(models.Model):
    titulo = models.CharField(max_length=90)
    subtitulo = models.CharField(max_length=90)
    texto = models.CharField(max_length=254)
    nombre= models.CharField(max_length=90)
    email= models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (f'titulo: {self.titulo}, subtitulo: {self.subtitulo}, texto: {self.texto}, nombre: {self.nombre}, email: {self.email}, fecha :{self.fecha}')

## Post List ##
class PosteoList(models.Model):
    titulo = models.CharField(max_length=90)
    subtitulo = models.CharField(max_length=90)
    texto = models.CharField(max_length=254)
    nombre= models.CharField(max_length=90)
    email= models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    email= models.CharField(max_length=50)
    
    def __str__(self):
        return (f'user: {self.user}, email: {self.email}')

class Avatar(models.Model):

    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/avatar/', null=True, blank=True)



### tests

