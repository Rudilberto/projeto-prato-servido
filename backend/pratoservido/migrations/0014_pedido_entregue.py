# Generated by Django 5.1.1 on 2024-10-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratoservido', '0013_cliente_remove_pedido_usuario_pedido_forma_pagamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entregue',
            field=models.BooleanField(default=False),
        ),
    ]
