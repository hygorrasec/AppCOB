from django.shortcuts import render


def create_competition(request):
    return render(request, 'create_competition/home.html')
