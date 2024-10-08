# Generated by Django 5.1.1 on 2024-10-01 00:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratoservido', '0011_remove_estabelecimento_proprietario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preparacao', models.BooleanField(default=False)),
                ('finalizado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('prato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pratoservido.prato')),
                ('pedido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pratoservido.pedido')),
            ],
        ),
    ]
