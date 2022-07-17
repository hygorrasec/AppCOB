from django.shortcuts import render


def register_result(request):
    return render(request, 'register_result/home.html')
