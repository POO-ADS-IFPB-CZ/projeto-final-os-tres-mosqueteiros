from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from paginas.models import  Curso, Aulas
from .forms import CursoForm,PerfilForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import AulaForm 
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm


class UsuarioListView(LoginRequiredMixin, ListView):
    login_url = 'login'  # Substitua pelo seu URL de login
    redirect_field_name = 'redirect_to'
    model = User
    template_name = 'usuario.html'  # O template a ser utilizado

    def get_queryset(self):
        # Retorna apenas o usuário logado
        return User.objects.filter(id=self.request.user.id)


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redirecione para a página que você deseja
    return redirect('login')  # Se for uma requisição GET, redireciona para a página inicial

"""
class CriarUsuario (CreateView):
	template_name="cadastrar.html"
	# model = User
	# fields = ['username','email','password']
	form_class = UsuarioForm
	success_url = reverse_lazy('login')

	def get_context_data(self, *args, **kwargs):
		context = super().get.context.data(*args, **kwargs)
		
		context['titulo'] = "Registro de novo usuário"
		context['botao'] = registrar

		return context
"""

def registrarUsuario(request):
    if request.method == 'POST':
        userform = UsuarioForm(request.POST)
        perfilform = PerfilForm(request.POST)
        if userform.is_valid() and perfilform.is_valid():
            user = userform.save()
            profile = perfilform.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')  # redirecione para a página de login ou outra
    else:
        userform = UsuarioForm()
        perfilform = PerfilForm()

    return render(request, 'cadastrar.html', {'userform': userform, 'perfilform': perfilform})

@login_required(login_url='')
def listar_cursos(request):
    template_name = 'listar-curso.html'
    cursos = Curso.objects.all()
    context= {
        'cursos': cursos
    } 
    return render(request,template_name,{'cursos': cursos})

@login_required(login_url='')
def criar_curso(request):
     if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES) # pega as informações do form
        if form.is_valid(): # se for valido
            curso = form.save(commit=False)  # Não salva ainda
            curso.usuario = request.user     # Associa o curso ao usuário logado
            curso.save() 
            
            messages.success(request, 'O curso foi criado com sucesso') 
            return HttpResponseRedirect(reverse('listar-curso')) 
        
     form = CursoForm() # senão carrega o formulario  
     return render(request, 'criar-curso.html', {"form": form}) 

@login_required(login_url='')
def curso_detalhes(request, id):
    template_name = 'curso-detalhes.html' # template
    curso = Curso.objects.get(id=id) # Metodo Get
    aulas = curso.aulas.all()  # Obtém todas as aulas associadas ao curso
    context = {
        'curso': curso,
        'aulas': aulas  # Passa as aulas associadas ao curso
    }
    return render(request, template_name, context) # render

@login_required(login_url='')
def curso_update(request, id):
    curso = get_object_or_404(Curso, id=id) # id do curso
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso) # pega as informações do form
    if form.is_valid(): # se for valido
        form.save() # salva
        
        messages.success(request, 'O curso foi atualizado com sucesso') # mensagem quando cria o curso
        return HttpResponseRedirect(reverse('curso-detalhes', args=[curso.id])) # coloquei para retornar curso-detalhes
         
    return render(request, 'criar-curso.html', {"form": form}) # nesse template



@login_required(login_url='')
def deletar_curso(request, id): 
    curso = Curso.objects.get(id=id) # pelo ID pega o objeto
    curso.delete() # deletar
    messages.success(request, 'O curso foi deletado com sucesso') # quando deleta curso
    return HttpResponseRedirect(reverse('listar-curso')) # retorna rota listar curso

@login_required(login_url='')
def adicionar_aula(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)  # Encontra o curso pelo ID
    if request.method == 'POST':
        form = AulaForm(request.POST, request.FILES)  # Suporte a arquivos se houver vídeo
        if form.is_valid():
            aula = form.save(commit=False)
            aula.curso = curso  # Associa a nova aula ao curso
            aula.save()
            return redirect('curso-detalhes', id=curso.id)  # Redireciona para os detalhes do curso
    else:
        form = AulaForm()

    return render(request, 'adicionar_aula.html', {'form': form, 'curso': curso})

@login_required(login_url='')
def deletar_aula(request, id):
    aula = Aulas.objects.get(id=id) # pelo ID pega o objeto
    idCurso = aula.curso.id
    aula.delete() # deletar

    messages.success(request, 'a aula foi deletada com sucesso')
    return redirect('curso-detalhes', idCurso)

@login_required(login_url='')
def aula_update(request, id):
    aula = get_object_or_404(Aulas, id=id) 
    form = AulaForm(request.POST or None, request.FILES or None, instance=aula) 
    if form.is_valid(): 
        form.save() 
        
        messages.success(request, 'a aula foi atualizado com sucesso') 
        return HttpResponseRedirect(reverse('curso-detalhes', args=[aula.curso.id])) 
         
    return render(request, 'adicionar_aula.html', {"form": form}) 