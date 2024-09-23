from django import forms
from .models import Curso, Aulas


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso 
        fields = ['titulo', 'descricao', 'image'] # ou'__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control' }),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5 }),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'titulo': 'Título do Curso',
            'descricao': 'Descrição do Curso',
            'image': 'Imagem do Curso',
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aulas
        fields = ['titulo', 'descricao', 'video'] 
