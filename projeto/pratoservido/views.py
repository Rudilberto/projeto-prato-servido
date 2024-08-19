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
    pratos = Prato.objects.filter(estabelecimento=estabelecimento)
    if request.method == 'POST':
        nome = request.POST.get('prato')
        preco = float(request.POST.get('preco'))
        ingredientes = request.POST.get('ingredientes')
        imagem = request.FILES.get('imagem')
        Prato.objects.create(nome=nome, preco=preco, ingredientes=ingredientes, imagem=imagem, estabelecimento=estabelecimento)
        messages.success(request, 'Prato criado com sucesso!')

        return redirect('adicionar_pratos')
    
    context = {'pratos': pratos}
    return render(request, 'pratoservido/adicionar_pratos.html', context)


@login_required
def remover_prato(request, id_prato):
    prato = Prato.objects.filter(id=id_prato).first()
    
    if not prato:
        messages.warning(request, 'Prato não encontrado!')
        return redirect('adicionar_pratos')
    
    prato.delete()
    messages.success(request, 'Prato removido com sucesso!')
    
    return redirect('adicionar_pratos')


@login_required
def informacoes_estabelecimento(request):
    usuario = request.user
    estabelecimento = Estabelecimento.objects.get(usuario=usuario)
    id = estabelecimento.id

    if request.method == 'POST':
        estabelecimento.nome = request.POST.get('estabelecimento')
        estabelecimento.telefone = request.POST.get('telefone')
        estabelecimento.endereco = request.POST.get('endereco')
        estabelecimento.descricao = request.POST.get('descricao')
        logo = request.FILES.get('logo')
        print(logo)
        if logo == None:
            logo = estabelecimento.logo
        else:
            estabelecimento.logo = logo
        estabelecimento.save()
        messages.success(request, 'Informações do estabelecimento alterados com sucesso!')

    context = {'estabelecimento': estabelecimento}
    return render(request, 'pratoservido/informacoes_estabelecimento.html', context)