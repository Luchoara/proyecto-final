from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PosteoForm, SignUpForm, UserEditForm, CuentaUsuarioForm
from .models import Posteo, Avatar 
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def mostrar_index(request):

    return render(request, 'index.html')

def login_index(request):

    imagen = Avatar.objects.filter(user=request.user.id)

    if imagen.exists():

            url = imagen[0].imagen.url #hay un problema aqui

    else:

            url = None

    return render(request,'index.html', {'url': url})


    
def mostrar_contact(request):
    
    return render(request,'contact.html')


def cursoPost(request):
    
    return render(request,'Posts.html')


@login_required
def crear_post(request):

    if request.method == 'POST':

        posteo = PosteoForm(request.POST)

        print('posteo')

        if posteo.is_valid():
        
            data = posteo.cleaned_data

            
            posteo  = Posteo (titulo=data['titulo'], texto=data['texto'])

            posteo.save()

            return render(request,'index.html')

    else:

        posteo = PosteoForm()

        print('formulario')

    return render(request,'Posts.html',{'posteo':posteo})


def buscar_post(request):

    return render(request,'buscador.html')



def buscador (request):
    if request.GET.get ('titulo', False):

        titulo  = request.GET ['titulo']
        
        post = Posteo.objects.filter(titulo__icontains=titulo)

        return render (request, 'buscador.html',{'post':post})
        
    else:
        respuesta = 'no hay datos'
    
    return render (request, 'buscador.html', {'respuesta':respuesta})
    


class PosteoList(ListView):

    model = Posteo
    template_name = 'mostrar_post.html'

class PosteoDetail(DetailView):

    model = Posteo
    template_name = 'posteo_detalle.html' 


def base(request):

    return render(request,'base.html')



class PosteoDeleteView(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = 'post_confirm_delete.html' 
    success_url = '/mostrarPost'
    

class PosteoUpdateView(LoginRequiredMixin, UpdateView):
    model = Posteo
    template_name = 'modificar_post.html' 
    success_url = '/mostrarPost'
    fields =['titulo', 'subtitulo','texto','nombre', 'email']
    

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = "registro.html"



def Perfil_usuario(request):

    usuario = request.user

    
@login_required
def editar_usuario(request):

    usuario = request.user
    if request.method == 'POST':

        usuario_form = UserEditForm(request.POST)
    
        if usuario_form.is_valid():
            informacion = usuario_form.cleaned_data
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion ['password2']
            

            usuario.save()
        
        return render(request,'index.html')


    else:
        
        usuario_form = UserEditForm(initial={'username': usuario.username, 'email': usuario.email})

    return render(request, 'admin_update.html', { 
            'form': usuario_form, 
            'usuario': usuario
            })

class AdminLoginView(LoginView):

    template_name = 'login.html'
    success_url = reverse_lazy('index')
    


class AdminLogoutView(LogoutView):

    template_name = 'logout.html'
    success_url = reverse_lazy('index')

def about(request):

    return render(request,'about.html')

def accountSettings(request):

    return render(request,'account_settings.html')