from django.db import models
from datetime import datetime

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=150, null=False, blank=False)
    preco = models.FloatField(null=True, blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    data_atualizacao = models.DateTimeField(default=datetime.now, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
