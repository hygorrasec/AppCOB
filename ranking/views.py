from django.shortcuts import render


def ranking(request):
    return render(request, 'ranking/home.html', context={
        'list': 'Aqui vai a lista de Ranking!'
    })


def modality(request, name):
    return render(request, 'ranking/modality.html', {'name': name})
