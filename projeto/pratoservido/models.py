from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    rua = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Rua: {self.rua}, Número: {self.numero}, Cidade: {self.cidade}-{self.estado}'


class Prato(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    ingrediente = models.TextField(max_length=500, null=True, blank=True)
    imagem = models.ImageField(upload_to='prato', default='prato/pratopadrao.webp')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome}'

    
class Cardapio(models.Model):
    prato = models.ManyToManyField(Prato,blank=True, related_name='estabelecimento')

    def __str__(self):
        return f'{self.estabelecimento.nome} - pratos: {self.prato.count()}'


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    proprietario = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', default='prato/logopratoservido.webp', null=True, blank=True)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    cardapio = models.OneToOneField(Cardapio, on_delete=models.SET_NULL, blank=True, null=True, related_name='cardapio')

    def __str__(self):
        return f'{self.nome} - proprietário: {self.proprietario}'
