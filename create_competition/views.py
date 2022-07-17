from django.shortcuts import render

from .models import CreateCompetition


def create_competition(request):
    athletes = CreateCompetition.objects.all()
    return render(request, 'create_competition/home.html', {'athletes': athletes})
