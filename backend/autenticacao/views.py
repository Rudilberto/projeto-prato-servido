from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from pratoservido.models import Estabelecimento
from django.utils.text import slugify 

# Create your views here.

def criar_conta(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        username = dados['username']
        email = dados['email']
        senha = dados['password']
        confirmacao_senha = dados['confirm_password']
        nome_estabelecimento = dados['estabelecimento']
        if not (username and email and senha and confirmacao_senha and nome_estabelecimento):
            messages.error(request, message='Preencha todos os campos!')

        else:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, message='E-mail inválido!')

            if senha != confirmacao_senha:
                messages.error(request, message='As senhas não coincidem!')
            
            else:
                usuario, criado = User.objects.get_or_create(username=username, email=email)
                if not criado:
                    messages.error(request, message='Usuário já existe')
                else:
                    usuario.set_password(senha)
                    usuario.save()
                    estabelecimento, criado = Estabelecimento.objects.get_or_create(usuario=usuario)
                    estabelecimento.usuario = usuario
                    estabelecimento.nome = nome_estabelecimento
                    estabelecimento.slug = slugify(nome_estabelecimento)
                    estabelecimento.save()
                    usuario = authenticate(username=username, password=senha)
                    login(request, usuario)
                    
                    return redirect('homepage')

    return render(request, 'autenticacao/criar_conta.html')

def fazer_login(request):
    if request.method == 'POST':
        dados = request.POST.dict()
        username = dados['username']
        senha = dados['password']
        usuario = authenticate(username=username, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('administracao')
        else:
            messages.error(request, 'nome de usuario ou senha errada!')
        return render(request, 'autenticacao/login.html')

    else:
        return render(request, 'autenticacao/login.html')

@login_required
def fazer_logout(request):
    logout(request)
    messages.info(request, 'Deslogado com sucesso!')
    return redirect('fazer_login')