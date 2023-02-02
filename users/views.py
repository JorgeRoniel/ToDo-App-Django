from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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