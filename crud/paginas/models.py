from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    image = models.ImageField('image/')
    criando_em = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self): #salvar com o titulo
        return self.titulo
    
    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']

class Aulas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    video = models.URLField(max_length=500)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='aulas')

    
    def save(self, *args, **kwargs):
        if 'watch?v=' in self.video:
            self.video = self.video.replace('watch?v=', 'embed/')
        super(Aulas, self).save(*args, **kwargs)
    


    def __str__(self):
        return f'{self.titulo} ({self.curso.nome})'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
=======
    image = models.ImageField(upload_to='image/', blank=True, null=True)
>>>>>>> d5fbf383bb29c3fe09467d01210f3ee6491284ff

    def __str__(self):
        return self.user.username