from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", views.inicio, name="inicio"),
    path("alta_historias", views.altaHistorias, name="crearHistoria"),
    path("historias", views.historias, name="historias"),
    path("formPersonas", views.informacion_personas, name="info_personas"),
    path("alta_personas", views.alta_personas),
    path("personas", views.persona, name="personas"),
    path("buscarPersona", views.buscarPersona),
    path('usuarios/', include("app_usuarios.urls")),
    path("leermas/<int:id>", views.leerHistorias, name="LeerMas"),
    path("about_me", views.aboutMe, name="AboutMe")
   
    
    
    
]
