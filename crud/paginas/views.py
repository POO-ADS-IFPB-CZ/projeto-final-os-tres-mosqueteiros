from django.shortcuts import render
from django.shortcuts import get_object_or_404
from paginas.models import  Curso
from .forms import CursoForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


def listar_cursos(request):
    template_name = 'listar-curso.html'
    cursos = Curso.objects.all()
    context= {
        'cursos': cursos
    } 
    return render(request,template_name,{'cursos': cursos})


def criar_curso(request):
     if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES) # pega as informações do form
        if form.is_valid(): # se for valido
            form = form.save(commit=False)
            form.save() 
            
            messages.success(request, 'O curso foi criado com sucesso') 
            return HttpResponseRedirect(reverse('listar-curso')) 
        
     form = CursoForm() # senão carrega o formulario  
     return render(request, 'criar-curso.html', {"form": form}) 

def curso_detalhes(request, id):
    template_name = 'curso-detalhes.html' # template
    curso = Curso.objects.get(id=id) # Metodo Get
    context = { # cria context para chamar no template
        'curso': curso
        }
    return render(request, template_name, context) # render

def curso_update(request, id):
    curso = get_object_or_404(Curso, id=id) # id do curso
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso) # pega as informações do form
    if form.is_valid(): # se for valido
        form.save() # salva
        
        messages.success(request, 'O post foi atualizado com sucesso') # mensagem quando cria o curso
        return HttpResponseRedirect(reverse('curso-detalhes', args=[curso.id])) # coloquei para retornar curso-detalhes
         
    return render(request, 'criar-curso.html', {"form": form}) # nesse template

from django.urls import reverse
from django.http import HttpResponseRedirect

def deletar_curso(request, id): 
    curso = Curso.objects.get(id=id) # pelo ID pega o objeto
    curso.delete() # deletar
    messages.success(request, 'O curso foi deletado com sucesso') # quando deleta post
    return HttpResponseRedirect(reverse('listar-curso')) # retorna rota post-list