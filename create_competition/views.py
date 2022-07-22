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
        # form = CreateForm()
        # print(f'FORM: {form}')
        getAthletes = CreateCompetition.objects.all()  # .order_by('-created_at')

        count_1 = 0
        count_2 = 0

        for i in getAthletes:
            if i.name_competition == '1':
                count_1 += 1
            elif i.name_competition == '2':
                count_2 += 1
            print(f'ID: {i.id}')
            print(f'ATLETA: {i.name_athlete}')
            print(f'COMPETIÇÃO: {i.name_competition}')
            print(f'IDADE: {i.age_athlete}')
            print(f'ALTURA: {i.height_athlete}')
            print(f'PESO: {i.weight_athlete}')
            print(f'DATA CADASTRO: {i.created_at}')

        print(f'TOTAL 100m rasos: {count_1}')
        print(f'TOTAL Lançamento de Dardo: {count_2}')

        return render(request, 'create_competition/pages/home.html',
                      context={
                          'if_competition_ok': False,
                          'athletes': getAthletes,
                          #   'form': form
                      })
