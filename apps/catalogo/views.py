from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from apps.catalogo.models import Produto
from apps.catalogo.forms import ProdutoForms

def index(request):
        produtos = Produto.objects.all()
        if not request.user.is_authenticated:
                messages.error(request, "Usuário não logado")
                return redirect('login')

        return render(request, 'catalogo/index.html', {"cards": produtos})

def produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'catalogo/produto.html', {"produto": produto})

def novo_produto(request):
        if not request.user.is_authenticated:
                messages.error(request, "Usuário não logado")
                return redirect('login')
        
        form = ProdutoForms()
        if request.method == 'POST':
                form.ProdutoForms(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request, 'Novo produto cadastrado com sucesso')
                        return redirect('index')
        return render(request, 'catalogo/novo_produto.html',{'form': form})

def editar_produto(request):
        pass

def deletar_produto(request):
        pass