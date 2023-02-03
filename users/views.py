from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def user_login(request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        usuario = authenticate(username=username, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválidas!')
    return redirect('/login/')

def user_logout(request):
    logout(request)
    return redirect('/login/')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html'