# Generated by Django 4.2 on 2023-04-22 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_remove_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ManyToManyField(to='catalogo.categoria'),
        ),
    ]
