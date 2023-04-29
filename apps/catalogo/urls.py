from django.urls import path, include
from django.contrib import admin
from apps.catalogo.views import ProdutoViewSet, CategoriaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('produtos', ProdutoViewSet, basename="Produtos")
router.register('categorias', CategoriaViewSet, basename="Categorias")

urlpatterns = [
        
        path('admin/', admin.site.urls),
        path('', include(router.urls)),

        # path('', index, name='index'),
        # path('produto/<int:produto_id>', produto, name='produto'),
        # path('novo-produto', novo_produto, name='novo_produto'),
        # path('editar-produto/<int:produto_id>', editar_produto, name='editar_produto'),
        # path('deletar-produto/<int:produto_id>', deletar_produto, name='deletar_produto'),
        
        # path('categoria', categoria, name='categoria'),
        # path('nova-categoria', nova_categoria, name='nova_categoria'),
        # path('editar-categoria/<int:categoria_id>', editar_categoria, name='editar_categoria'),
        # path('deletar-categoria/<int:categoria_id>', deletar_categoria, name='deletar_categoria'),
]
