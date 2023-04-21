from django.urls import path
from apps.catalogo.views import index, produto, novo_produto, editar_produto, deletar_produto

urlpatterns = [
        path('', index, name='index'),
        path('produto/<int:produto_id', produto, name='produto'),
        path('novo-produto', novo_produto, name='novo_produto'),
        path('editar-produto', editar_produto, name='editar_produto'),
        path('deletar-produto', deletar_produto, name='deletar_produto'),
]