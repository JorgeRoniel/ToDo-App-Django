from django import forms
from .models import Tarefa

class Taskform(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('titulo', 'descricao')