from django.db import models
from django.contrib.auth.models import User  
from django.db.models import Sum


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
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ingredientes = models.TextField(max_length=500, null=True, blank=True)
    imagem = models.ImageField(upload_to='prato', default='prato/pratopadrao.webp')
    ativo = models.BooleanField(default=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, related_name='pratos')

    def __str__(self):
        return f'{self.nome} - ativo={self.ativo} - {self.estabelecimento.nome}'
    

class Cliente(models.Model):
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    

class Pedido(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
    ('CARTAO', 'Cartão'),
    ('PIX', 'PIX'),
    ('DINHEIRO', 'Dinheiro'),]

    forma_pagamento = models.CharField(
        max_length=10,
        choices=FORMA_PAGAMENTO_CHOICES,
        null=True, blank=True,
    )

    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    bairro = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    estabelecimento = models.ForeignKey(Estabelecimento, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Id do cliente: {self.cliente.id} - Estabelecimento: {self.estabelecimento.nome} - finalizado={self.status.finalizado} - entregue={self.status.entregue}'
    
    @property
    def quantidade_total(self):
        return ItensPedido.objects.filter(pedido=self).aggregate(Sum('quantidade'))['quantidade__sum'] or 0

    @property
    def preco_total(self):
        return ItensPedido.objects.filter(pedido=self).aggregate(Sum('quantidade_total'))['quantidade_total__sum'] or 0
    

class StatusPedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='status')
    finalizado = models.BooleanField(default=False)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    preparacao = models.BooleanField(default=False)
    data_entrega = models.DateTimeField(null=True, blank=True)
    entregue = models.BooleanField(default=False)

    
class ItensPedido(models.Model):
    prato = models.ForeignKey(Prato, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Id do pedido={self.pedido.id}'
    
    @property 
    def preco_total(self):
        preco_total = self.quantidade * self.prato.preco
        return preco_total