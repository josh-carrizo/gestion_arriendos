from django.shortcuts import render,redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import login
from .models import Perfil
from django.contrib import messages


# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.create(
                usuario=user,
                nombres=form.cleaned_data['nombres'],
                apellidos=form.cleaned_data['apellidos'],
                rut=form.cleaned_data['rut'],
                direccion=form.cleaned_data['direccion'],
                telefono=form.cleaned_data['telefono'],
                correo_electronico=form.cleaned_data['correo_electronico'],
                tipo_usuario=form.cleaned_data['tipo_usuario']
            )
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente. ¡Bienvenido!')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def home(request):
    return render(request, 'home.html')
