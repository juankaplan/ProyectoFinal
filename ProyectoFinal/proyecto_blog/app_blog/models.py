from django.db import models

    
    
class Textos(models.Model):
    titulo = models.CharField(max_length=80, default="")
    subtitulo = models.CharField(max_length=100, default="")
    texto = models.TextField()
    autor = models.CharField(max_length=20, default="")
    fecha = models.DateField(auto_now=True)
    def __str__(self):
        return f"Autor: {self.autor} - Titulo: {self.titulo}"
    


class Personas(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    nacionalidad = models.CharField(max_length=20)
    edad = models.IntegerField()
    texto = models.CharField(max_length=200, default="")
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"
    
    

    
