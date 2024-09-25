from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário chamado ' + username)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')


def login(request):
    if request.method == "GET":
        return render(request, template_name='login.html')
    else:
        username = request.POST.get('username')

        senha = request.POST.get('password')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('AUTENTICADO')
        else:
            return HttpResponse('EMAIL OU SENHA INVALIDOS')


@login_required(login_url="/auth/login/")
def entrou(request):
    return HttpResponse('ENTROU NA PÁGINA!')
