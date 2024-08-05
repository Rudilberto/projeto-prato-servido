from django.shortcuts import render, redirect
from .models import *

def homepage(request):
    return render(request, 'pratoservido/homepage.html')

def estabelecimento(request):
    estabelecimentos = Estabelecimento.objects.all()

    context = {'estabelecimentos': estabelecimentos}
    return render(request, 'pratoservido/estabelecimento.html', context)
