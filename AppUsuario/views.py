from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PosteoForm, SignUpForm, UserEditForm
from .models import Posteo, Usuario, Avatar
from django.urls import reverse_lazy
from .forms import Avatar_Form, CuentaUsuarioForm



# Create your views here.
def mostrar_index(request):

    avatar = Avatar.objects.filter(user=request.user.id)

    if avatar.exists():

            url = avatar[0].imagen.url
            print('usuarioExiste')
    else:

            url = None

    return render(request, 'index.html', {'url': url})


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


#def buscar_post(request):

#    return render(request,'buscador.html')



def buscador(request):

    if request.GET.get('titulo', False):

        titulo  = request.GET['titulo']
        
        post = Posteo.objects.filter(titulo__icontains=titulo)
        
        return render(request, 'buscador.html',{'post':post})
        
    else:
        respuesta = print('no hay datos')
        
    return render (request, 'buscador.html', {'respuesta':respuesta})
    

def base(request):

    return render(request,'base.html')

    
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

def about(request):

    return render(request,'about.html')
    


class PosteoList(ListView):
    model = Posteo
    template_name = 'mostrar_post.html'

class PosteoDetail(DetailView):

    model = Posteo
    template_name = 'posteo_detalle.html' 


class PosteoDeleteView(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = 'post_confirm_delete.html' 
    success_url = '/mostrarpost'
    

class PosteoUpdateView(LoginRequiredMixin, UpdateView):
    model = Posteo
    template_name = 'modificar_post.html' 
    success_url = '/mostrarpost'
    fields =['titulo', 'subtitulo','texto','nombre', 'email']
    

class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = "registro.html"

class AdminLoginView(LoginView):

    template_name = 'login.html'
    success_url = ''
    


class AdminLogoutView(LogoutView):

    template_name = 'logout.html'
    success_url = reverse_lazy('index')



### <----->

def test(request):

    return render(request,'test.html')

def Cuenta_Detail(request):
<<<<<<< Updated upstream
    
    usuario = Usuario.objects.all()

    avatar = Avatar.objects.filter(user=request.user.id)

    if avatar.exists():

            url = avatar[0].imagen.url
            print('usuarioExiste')
    else:

            url = None

    return render(request, 'account_detail.html', {'usuario': usuario, 'url': url})
    
    

=======

    usuario = Usuario.objects.all()

    avatar = Avatar.objects.filter(user=request.user.id)

    url = avatar[0].imagen.url

    return render (request, 'account_detail.html', {'url': url, 'usuario':usuario})
>>>>>>> Stashed changes

class AvatarView(TemplateView):

    template_name = 'add_imagen.html'


def add_avatar(request):

    if request.method == 'POST':

        miAvatar = Avatar_Form(request.POST, request.FILES)

        if miAvatar.is_valid():

            usuario = request.user

            avatar = Usuario.objects.filter(user=usuario)

            file = miAvatar.cleaned_data

            if len(avatar) > 0:

                avatar = avatar[0]
                avatar.imagen = file['img']
                avatar.save()

                avatar = Usuario.objects.filter(user=request.user)

                img = avatar[0].imagen.url

            else:

                avatar = usuario(user=usuario, imagen=miAvatar.cleaned_data['img'])
                avatar.save()

                img = None

        return render(request, 'index.html', {'img':img})
        
        return redirect('account_detail.html')

    else:

        miAvatar = Avatar_Form()

        img = None
        
        return render(request, 'add_imagen.html', {'miAvatar': miAvatar, 'img': img}) #


def ver_avatar(request):

    if request.GET.get('imagen', False):

        avatar = Avatar.objects.filter(user=request.user)

        if len(avatar) >= 0:
            
                img = avatar[0].imagen.url

        else:

                img = None

        return render(request, 'add_imagen.html', {'img':img})
    else:
        print('no se ve')