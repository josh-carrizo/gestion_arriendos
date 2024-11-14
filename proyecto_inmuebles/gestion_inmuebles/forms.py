from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Perfil

class RegistroUsuarioForm(UserCreationForm):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=12)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    correo_electronico = forms.EmailField()
    tipo_usuario = forms.ChoiceField(choices=Perfil.TIPO_USUARIO)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario']
