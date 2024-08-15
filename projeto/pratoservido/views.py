from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

def homepage(request):
    return render(request, 'pratoservido/homepage.html')

def estabelecimento(request):
    estabelecimentos = Estabelecimento.objects.all()

    context = {'estabelecimentos': estabelecimentos}
    return render(request, 'pratoservido/estabelecimento.html', context)


def cardapio(request, slug=None):
    try:
        estabelecimento = Estabelecimento.objects.get(slug=slug) 
        pratos = estabelecimento.pratos.filter(ativo=True)
    except  Estabelecimento.DoesNotExist:
        return redirect('estabelecimento')
    
    context = {'estabelecimento': estabelecimento, 'pratos': pratos}
    return render(request, 'pratoservido/cardapio.html', context)


@login_required
def administracao(request):

    context = {}
    return render(request, 'pratoservido/administracao.html', context)


@login_required
def adicionar_pratos(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.get(usuario=usuario)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = float(request.POST.get('preco'))
        ingredientes = request.POST.get('ingredientes')
        imagem = request.FILES.get('imagem')
        Prato.objects.create(nome=nome, preco=preco, ingredientes=ingredientes, imagem=imagem, estabelecimento=estabelecimento)
        messages.success(request, 'Prato criado com sucesso!')

        return redirect('adicionar_pratos')
    
    return render(request, 'pratoservido/adicionar_pratos.html')


@login_required
def informacoes_estabelecmento(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.filter(usuario=usuario)

    context = {'estabelecimento': estabelecimento}
    return render(request, 'pratoservido/informacoes_estabelecimento.html', context)