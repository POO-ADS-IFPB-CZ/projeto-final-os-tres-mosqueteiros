from django import forms
from .models import Curso, Aulas
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



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
        
        
class UsuarioForm(UserCreationForm):
	email = forms.EmailField(max_length=100)

	class Meta:
		model = User
		fields = ['username','email','password1','password2']
  