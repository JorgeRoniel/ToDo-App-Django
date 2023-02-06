from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Tarefa(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    done = models.CharField(max_length=5, choices=STATUS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)