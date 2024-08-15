from django.urls import path  
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('estabelecimento/', estabelecimento, name='estabelecimento'),
    path('estabelecimento/<slug:slug>/', cardapio, name='cardapio'),
    
    path('administracao/', administracao, name='administracao'),
    path('administracao/adicionar_pratos', adicionar_pratos, name='adicionar_pratos'),
    path('administracao/informacoes_estabelecimento', informacoes_estabelecmento, name='informacoes_estabelecmento'),
]