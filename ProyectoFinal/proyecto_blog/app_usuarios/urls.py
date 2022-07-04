from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.login_request, name= "principio"),
    path("login_request", views.login_request, name="login"),
    path("register", views.registro_usuario, name="registrarse"),
    path("logout", LogoutView.as_view(template_name="inicio_sesion.html"), name= "Logout"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil" )
    
    
    
    
    
]