from django.urls import path  
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('estabelecimento/', estabelecimento, name='estabelecimento'),
    path('estabelecimento/<slug:slug>/', cardapio, name='cardapio'),
    
    path('administracao/', administracao, name='administracao'),
    path('administracao/adicionar_pratos', adicionar_pratos, name='adicionar_pratos'),
    path('remover_prato/<int:id_prato>/', remover_prato, name='remover_prato'),

    path('administracao/informacoes_estabelecimento', informacoes_estabelecimento, name='informacoes_estabelecimento'),
]