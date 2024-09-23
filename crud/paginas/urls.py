from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.listar_cursos,name='listar-curso'),
    path('criar-curso', views.criar_curso, name='criar-curso'),
    path('curso-detalhes/<int:id>/', views.curso_detalhes, name='curso-detalhes'),
    path('curso-update/<int:id>', views.curso_update, name='curso-update'),
    path('deletar-curso/<int:id>/', views.deletar_curso, name='deletar-curso'),
    
    # URLS relacionado as Aulas 
    path('curso/<int:curso_id>/adicionar_aula/', views.adicionar_aula, name='adicionar_aula'),
    path('aula/deletar/<int:id>/', views.deletar_aula, name='deletar_aula'),
    
    path('login/', auth_views.LoginView.as_view(
         template_name='form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]