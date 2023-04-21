from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@mail.com"
            }
        )
    )
    senha1=forms.CharField(
        label="Senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha2=forms.CharField(
        label="Confirmar senha",
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite novamente sua senha"
            }
        )
    )
