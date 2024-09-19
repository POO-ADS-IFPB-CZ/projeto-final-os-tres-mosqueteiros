from django import forms
from .models import Curso, Aulas

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso 
        fields = ['titulo', 'descricao', 'image'] # ou'__all__'

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aulas
        fields = ['titulo', 'descricao', 'video'] 