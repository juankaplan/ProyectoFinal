from django import forms


class form_texto(forms.Form):
      titulo = forms.CharField(max_length=80)
      subtitulo = forms.CharField(max_length=100)
      texto = forms.CharField(widget=forms.Textarea)
      autor = forms.CharField(max_length=20)
      
      

class form_personas(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    texto = forms.CharField(max_length=200)
    


