from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def quienesSom(request):
    return render(request, 'quienesSom.html')

def galeria(request):
    return render(request, 'galeria.html')

def cerrar(request):
    logout(request)
    return redirect('/')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="inicio")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)


