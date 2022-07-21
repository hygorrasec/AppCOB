from django.shortcuts import render

from .forms import CreateForm
from .models import CreateCompetition


def create_competition(request):
    print(f'MÉTODO: {request.method}')
    if request.method == 'POST':
        form = CreateForm(request.POST)
        print(form)
        if form.is_valid():
            print('ENTROU!')
            form.save()
            form = CreateForm()
            getAthletes = CreateCompetition.objects.all()  # .order_by('-created_at')
            return render(request, 'create_competition/pages/home.html',
                          context={
                              'athletes': getAthletes,
                              'form': form
                          })
        else:
            print('APRESENTOU UM ERRO!')

    else:
        form = CreateForm()
        # print(f'FORM: {form}')
        getAthletes = CreateCompetition.objects.all()  # .order_by('-created_at')
        for i in getAthletes:
            print(f'ATLETA: {i.name_athlete}')
            print(f'COMPETIÇÃO: {i.name_competition}')
            print(f'IDADE: {i.age_athlete}')
            print(f'ALTURA: {i.height_athlete}')
            print(f'PESO: {i.weight_athlete}')
            print(f'DATA CADASTRO: {i.created_at}')

        return render(request, 'create_competition/pages/home.html',
                      context={
                          'athletes': getAthletes,
                          'form': form
                      })
