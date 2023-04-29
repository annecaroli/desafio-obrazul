from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from apps.catalogo.models import Produto, Categoria
from apps.catalogo.forms import ProdutoForms, CategoriaForms
from rest_framework import viewsets, generics
from serializer import ProdutoSerializer, CategoriaSerializer


def index(request):
        produtos = Produto.objects.all()
        if not request.user.is_authenticated:
                messages.error(request, "Usuário não logado")
                return redirect('login')

        return render(request, 'catalogo/index.html', {"cards": produtos})

def produtos(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'catalogo/produto.html', {"produto": produto})

def novo_produto(request):
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

        form = ProdutoForms
        if request.method == 'POST':
                form = ProdutoForms(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Novo produto cadastrado com sucesso')
                        return redirect('index')

        return render(request, 'catalogo/novo_produto.html', {'form': form})

def editar_produto(request, produto_id):
        produto = Produto.objects.get(id=produto_id)
        form = ProdutoForms(instance=produto)

        if request.method == 'POST':
                form = ProdutoForms(request.POST, instance=produto)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Produto editado com sucesso')
                        return redirect('index')
        return render(request, 'catalogo/editar_produto.html', {'form': form, 'produto_id': produto_id})

def deletar_produto(request, produto_id):
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        messages.success(request, 'Produto deletado com sucesso')
        
        return render(request, 'catalogo/index.html')

def categoria(request):
        categorias = Categoria.objects.all()
        if not request.user.is_authenticated:
                messages.error(request, "Usuário não logado")
                return redirect('login')

        return render(request, 'catalogo/categoria.html', {"cards": categorias})

def nova_categoria(request):
        if not request.user.is_authenticated:
                messages.error(request, 'Usuário não logado')
                return redirect('login')

        form = CategoriaForms
        if request.method == 'POST':
                form = CategoriaForms(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Nova categoria cadastrada com sucesso')
                        return redirect('categoria')

        return render(request, 'catalogo/nova_categoria.html', {'form': form})

def editar_categoria(request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        form = CategoriaForms(instance=categoria)

        if request.method == 'POST':
                form = CategoriaForms(request.POST, instance=categoria)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Categoria editada com sucesso')
                        return redirect('categoria')
        return render(request, 'catalogo/editar_categoria.html', {'form': form, 'categoria_id': categoria_id})

def deletar_categoria(request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        categoria.delete()
        messages.success(request, 'Categoria deletada com sucesso')
        
        return render(request, 'catalogo/categoria.html')


class ProdutoViewSet(viewsets.ModelViewSet):
        """exibe todos os produtos"""
        queryset = Produto.objects.all()
        serializer_class = ProdutoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
        """exibe todas as categorias"""
        queryset = Categoria.objects.all()
        serializer_class = CategoriaSerializer
