from django.shortcuts import render


def ranking(request):
    return render(request, 'ranking/pages/home.html')


def modality(request, id):
    return render(request, 'ranking/pages/modality.html', context={
        'id': id
    })
