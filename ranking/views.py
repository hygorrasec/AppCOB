from django.shortcuts import render


def ranking(request):
    return render(request, 'ranking/pages/home.html', context={
        'list': 'Aqui vai a lista de Ranking!'
    })


def modality(request, name):
    return render(request, 'ranking/pages/modality.html', {'name': name})
