from django.db import models
from django.utils import timezone

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    image = models.ImageField('image/')
    criando_em = models.DateTimeField(default=timezone.now)

    def __str__(self): #salvar com o titulo
        return self.titulo
    
    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

class Aulas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    video = models.FileField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='aulas')
    


    def __str__(self):
        return f'{self.titulo} ({self.curso.nome})'
