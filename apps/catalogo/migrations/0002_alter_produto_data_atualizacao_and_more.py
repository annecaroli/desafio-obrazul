# Generated by Django 4.2 on 2023-04-21 01:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data_atualizacao',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='produto',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
