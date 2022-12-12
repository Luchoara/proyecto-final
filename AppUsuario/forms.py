from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm
from django import forms

class PosteoForm(forms.Form):
    
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=400)  
    nombre = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    fecha = forms.DateField(initial=datetime.date.today)

class PostearForm(forms.Form):

    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    texto = forms.CharField(max_length=400)  
    nombre = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    fecha = forms.DateField(initial=datetime.date.today)


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:'' for k in fields} 


class UserEditForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k:'' for k in fields} 

class CuentaUsuarioForm(ModelForm):
    
    class Meta:
        model = User
        fields =  '__all__'
        exclude = [ 'user'] 

class avatarForm(ModelForm):

    avatar_img = forms.ImageField()





