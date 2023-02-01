from django.db import models

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