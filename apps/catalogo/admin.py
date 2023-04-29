from django.contrib import admin
from apps.catalogo.models import Categoria, Produto

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')

admin.site.register(Categoria, Categorias)

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'preco', 'data_cadastro', 'data_atualizacao')
    list_display_links = ('id', 'nome', 'descricao', 'preco', 'data_cadastro', 'data_atualizacao')

admin.site.register(Produto, Produtos)
