from django import forms
from apps.catalogo.models import Produto
from apps.catalogo.models import Categoria

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        #fields= ['nome']
        exclude = []
        labels = {
            'nome': "Nome"
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'})
        }

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_atualizacao',]
        labels = {
            'descricao': "Descrição",
            'preco': "Preço",
            'data_cadastro': "Data de Cadastro",
            'categoria': "Categoria"
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'preco': forms.TextInput(attrs={'class':'form-control'}),
            'data_cadastro': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class':'form-control',
                    'type':'date'
                },
            ),
            'categoria': forms.Select(attrs={'class':'form-control'})
        }
