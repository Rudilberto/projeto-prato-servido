from django.db import models
from django.contrib.auth.models import User  


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=400, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', default='logo/logopratoservido.webp', null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome}'
        

class Prato(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ingredientes = models.TextField(max_length=500, null=True, blank=True)
    imagem = models.ImageField(upload_to='prato', default='prato/pratopadrao.webp')
    ativo = models.BooleanField(default=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='pratos')

    def __str__(self):
        return f'{self.nome} - ativo={self.ativo} - {self.estabelecimento.nome}'
