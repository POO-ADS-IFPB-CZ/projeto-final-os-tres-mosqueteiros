from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso 
        fields = ['titulo', 'descricao', 'image'] # ou'__all__'