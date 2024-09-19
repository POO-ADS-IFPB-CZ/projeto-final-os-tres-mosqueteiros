from django.urls import path
from . import views 

urlpatterns = [
    path('',views.listar_cursos,name='listar-curso'),
    path('criar-curso', views.criar_curso, name='criar-curso'),
    path('curso-detalhes/<int:id>/', views.curso_detalhes, name='curso-detalhes'),
    path('curso-update/<int:id>', views.curso_update, name='curso-update'),
    path('deletar-curso/<int:id>/', views.deletar_curso, name='deletar-curso'),
]