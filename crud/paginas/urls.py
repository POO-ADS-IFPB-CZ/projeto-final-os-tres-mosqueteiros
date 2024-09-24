from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .views import CriarUsuario


urlpatterns = [
    path('home',views.listar_cursos,name='listar-curso'),
    path('criar-curso', views.criar_curso, name='criar-curso'),
    path('curso-detalhes/<int:id>/', views.curso_detalhes, name='curso-detalhes'),
    path('curso-update/<int:id>', views.curso_update, name='curso-update'),
    path('deletar-curso/<int:id>/', views.deletar_curso, name='deletar-curso'),
    
    # URLS relacionado as Aulas 
    path('curso/<int:curso_id>/adicionar_aula/', views.adicionar_aula, name='adicionar_aula'),
    path('aula/deletar/<int:id>/', views.deletar_aula, name='deletar_aula'),
    path('aula-update/<int:id>', views.aula_update, name='aula_update'),
    
    path('', auth_views.LoginView.as_view(
         template_name='form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrarUsuario, name='registrar'),
]