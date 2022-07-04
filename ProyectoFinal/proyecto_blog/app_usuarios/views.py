from re import template
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from app_usuarios.forms import UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            contraseña = formulario.cleaned_data.get("password")
            
            user = authenticate(username = usuario, password = contraseña)
            
            if user is not None:
                login(request, user)
                return render(request, "inicio.html")
            
        else:
                return render(request, "errorUsuario.html")
    
    formulario = AuthenticationForm()
    return render(request, "inicio_sesion.html", {"form": formulario})     





def registro_usuario(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)  
        print(formulario)
        
        if formulario.is_valid:
            try:
                formulario.save()
                return render(request, "inicio_sesion.html")
            except:
                return render(request, "errorUsuario.html")
        else:
            return HttpResponse("Valores no validos")
    else:
         formulario = UserCreationForm()
         return render(request, "register.html", {"form": formulario})
     
     
     
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion["email"]
            contraseña = informacion["password1"]
            usuario.set_password(contraseña)
            usuario.save()
        
            return render(request, "inicio.html")
        
        return HttpResponse("error")
            
    
    
    
    else:
        
        return render(request, "editarPerfil.html", {"email": usuario.email })
            