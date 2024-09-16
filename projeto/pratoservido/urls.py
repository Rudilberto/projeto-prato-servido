from django.urls import path  
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('estabelecimento/', estabelecimento, name='estabelecimento'),
    path('estabelecimento/<slug:slug>/', cardapio, name='cardapio'),
    
    path('administracao/', administracao, name='administracao'),
    path('administracao/gerenciar_pratos', gerenciar_pratos, name='gerenciar_pratos'),
    path('remover_prato/<int:id_prato>/', remover_prato, name='remover_prato'),
    path('ativar_prato/<int:id_prato>/', ativar_prato, name='ativar_prato'),

    path('administracao/informacoes_estabelecimento', informacoes_estabelecimento, name='informacoes_estabelecimento'),
]