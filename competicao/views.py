from django.shortcuts import render


def home(request):
    return render(request, 'competicao/home.html', context={
        'atleta': 'Hygor Rasec'
    })
