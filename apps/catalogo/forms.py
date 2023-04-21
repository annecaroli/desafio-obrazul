from django import forms
from apps.catalogo.models import Produto

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ['data_atualizacao',]
        labels = {
            'descricao': "Descrição",
            'preco': "Preço",
            'data_cadastro': "Data de Cadastro"
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
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }
