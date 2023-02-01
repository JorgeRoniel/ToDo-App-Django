from django.contrib import admin
from .models import Tarefa
# Register your models here.

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_criacao')

admin.site.register(Tarefa, TarefaAdmin)