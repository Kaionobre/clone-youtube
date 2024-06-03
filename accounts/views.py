from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .forms import LoginForms, CadastroForms

class LoginView(View):
    def get(self, request):
        form = LoginForms()
        return render(request, 'accounts/pages/login.html', {"form": form})

    def post(self, request):
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} logado com sucesso!")
                return redirect('home')
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')
        else:
            messages.error(request, "Formulário inválido")
            return redirect('login')


class CadastroView(View):
    def get(self, request):
        form = CadastroForms()
        return render(request, 'accounts/pages/cadastro.html', {"form": form})

    def post(self, request):
        form = CadastroForms(request.POST)
        if form.is_valid():
            if form.cleaned_data["senha_1"] != form.cleaned_data["senha_2"]:
                messages.error(request, "Senhas não são iguais")
                return redirect('cadastro')

            nome = form.cleaned_data["nome_cadastro"]
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["senha_1"]

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )

            usuario.save()

            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect('login')
        else:
            messages.error(request, "Formulário inválido")
            return redirect('cadastro')
