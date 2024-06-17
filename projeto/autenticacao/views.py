from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def fazer_login(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        print(dados)
        username = dados['username']
        password = dados['password']
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, 'logado com sucesso!')
            return redirect('homepage')
        else:
            messages.success(request, 'nome de usuario ou senha errada!')
        return render(request, 'autenticacao/login.html')

    else:
        return render(request, 'autenticacao/login.html')

def fazer_logout(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return render(request, 'pratoservido/homepage.html')