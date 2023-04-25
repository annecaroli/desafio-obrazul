from django.urls import path, include
from apps.catalogo.views import index, produto, novo_produto, editar_produto, deletar_produto, categoria, nova_categoria, editar_categoria, deletar_categoria
from apps.catalogo.views import ProdutoViewSet, CategoriaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produto', ProdutoViewSet, basename="Produto")
router.register('categoria', CategoriaViewSet, basename="Categoria")

urlpatterns = [
        path('', index, name='index'),
        
        path('produto/<int:produto_id>', produto, name='produto'),
        path('novo-produto', novo_produto, name='novo_produto'),
        path('editar-produto/<int:produto_id>', editar_produto, name='editar_produto'),
        path('deletar-produto/<int:produto_id>', deletar_produto, name='deletar_produto'),
        
        path('categoria', categoria, name='categoria'),
        path('nova-categoria', nova_categoria, name='nova_categoria'),
        path('editar-categoria/<int:categoria_id>', editar_categoria, name='editar_categoria'),
        path('deletar-categoria/<int:categoria_id>', deletar_categoria, name='deletar_categoria'),
]