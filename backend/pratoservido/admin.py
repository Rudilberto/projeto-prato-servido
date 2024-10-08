from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Prato)
admin.site.register(Estabelecimento)
admin.site.register(ItensPedido)
admin.site.register(Pedido)