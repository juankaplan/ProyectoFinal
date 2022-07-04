from re import template
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from app_blog.models import Textos, Personas
from app_blog.forms import  form_texto,  form_personas
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "inicio.html")
    
    



@login_required
def altaHistorias(request):
    if request.method == "POST":
        mi_Formulario = form_texto(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            informacion_formulario = mi_Formulario.cleaned_data
            texto = Textos(titulo = informacion_formulario["titulo"], subtitulo = informacion_formulario["subtitulo"], texto = informacion_formulario["texto"], autor = informacion_formulario["autor"])
            texto.save()
            Formulario = form_texto()
            return render(request, "crear_historias.html", {"form": Formulario})
        else: 
            return HttpResponse("error")
        
    else: 
        miFormulario = form_texto()
        return render(request, "crear_historias.html", {"form": miFormulario})
 
 
@login_required       
def historias(request):
    historias = Textos.objects.all()
    datos = {"historias": historias}
    return render(request, "historias.html", datos)

 
 
       
@login_required       
def informacion_personas(request):
    return render(request, "IngresarPersonas.html")



@login_required
def alta_personas(request):
    if request.method == "GET":
        mi_formulario = form_personas(request.GET)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion_formulario = mi_formulario.cleaned_data
            persona = Personas(nombre = informacion_formulario["nombre"], apellido = informacion_formulario["apellido"],  nacionalidad = informacion_formulario["nacionalidad"], edad = informacion_formulario["edad"], texto = informacion_formulario["texto"])
            persona.save()
            return render(request, "IngresarPersonas.html")
    



@login_required
def persona(request):
    return render(request, "personas.html")




@login_required
def buscarPersona(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        persona = Personas.objects.filter(nombre = nombre, apellido = apellido )
        datos = {"persona": persona}
        return render(request, "personas.html", datos)
    


@login_required
def leerHistorias(request, id):
    historia = Textos.objects.get(id = id)
    return render(request, "leer_historia.html", {"historia": historia})    



@login_required
def aboutMe(request):
  return render(request, "about_me.html")  

