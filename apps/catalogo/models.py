from django.db import models
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return str(self.nome)
    
class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=150, null=False, blank=False)
    preco = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)
    data_atualizacao = models.DateTimeField(default=datetime.now, blank=False)
    categoria = models.ForeignKey(
        to=Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        default="Sem Categoria",
        related_name='categoria'
    )

    def __str__(self):
        return str(self.nome)
