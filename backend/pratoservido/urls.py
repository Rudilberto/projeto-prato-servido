from django.urls import path  
from .views import *
from .views_htmx import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('estabelecimento/', estabelecimento, name='estabelecimento'),
    path('estabelecimento/<slug:slug>/', cardapio, name='cardapio'),
    
    path('administracao/', administracao, name='administracao'),
    path('administracao/gerenciar_pratos', gerenciar_pratos, name='gerenciar_pratos'),
    path('remover_prato/<int:id_prato>/', remover_prato, name='remover_prato'),
    path('ativar_prato/<int:id_prato>/', ativar_prato, name='ativar_prato'),

    path('administracao/informacoes_estabelecimento', informacoes_estabelecimento, name='informacoes_estabelecimento'),

    path('finalizar_carrinho/<int:id_pedido>', finalizar_carrinho, name='finalizar_carrinho'),
]

urlpatterns_htmx = [
    path('carrinho/<int:id_estabelecimento>', carrinho, name='carrinho'),
    path('add_carrinho/<int:id_prato>', add_carrinho, name='add_carrinho'),
    path('remover_carrinho/<int:id_prato>', remover_carrinho, name='remover_carrinho'),
    path('excluir_carrinho/<int:id_prato>', excluir_carrinho, name='excluir_carrinho'),

    path('cartao_pedidos', cartao_pedidos, name='cartao_pedidos'),
    path('preparar_pedido/<int:id_pedido>', preparar_pedido, name='preparar_pedido'),
    path('entregar_pedido/<int:id_pedido>', entregar_pedido, name='entregar_pedido'),
]

urlpatterns += urlpatterns_htmx