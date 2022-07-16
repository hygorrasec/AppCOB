from django.shortcuts import render


def home(request):
    return render(request, 'competicao/home.html', context={
        'welcome': 'Olá, seja bem-vindo(a)!'
    })


def modalidade(request, name):
    return render(request, 'competicao/modalidade.html', {'name': name})
