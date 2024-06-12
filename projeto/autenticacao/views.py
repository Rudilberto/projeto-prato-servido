from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def fazer_login(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        username = dados['username']
        password = dados['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            redirect('homepage')
        else:
            pass
        return render(request, 'autenticacao/login.html')

    else:
        return render(request, 'autenticacao/login.html')

def fazer_logout(request):
    logout(request)
    return render(request, 'autenticacao/logout.html')