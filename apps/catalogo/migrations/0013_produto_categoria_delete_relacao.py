# Generated by Django 4.2 on 2023-04-25 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_remove_produto_categoria_relacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='catalogo.categoria'),
        ),
        migrations.DeleteModel(
            name='Relacao',
        ),
    ]
