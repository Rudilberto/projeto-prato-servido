# Generated by Django 5.0.6 on 2024-08-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pratoservido', '0002_cardapio_prato_estabelecimento_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='prato',
            field=models.ManyToManyField(blank=True, related_name='estabelecimento', to='pratoservido.prato'),
        ),
    ]
