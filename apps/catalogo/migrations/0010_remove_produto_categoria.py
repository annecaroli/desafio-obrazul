# Generated by Django 4.2 on 2023-04-22 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_alter_produto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
    ]
