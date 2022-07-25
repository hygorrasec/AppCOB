from distutils.ccompiler import new_compiler  # noqa: F401

from django.shortcuts import render

from .forms import CreateForm
from .models import Competition, CreateCompetition  # noqa: F401


def create_competition(request):
    print(f'MÉTODO: {request.method}')
    if request.method == 'POST':
        form = CreateForm(request.POST)
        print(form)
        if form.is_valid():
            print('ENTROU!')
            form.save()
            form = CreateForm()
            getAthletes = CreateCompetition.objects.all()  # .order_by('-created_at')  # noqa: E501
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

        # Criando nova competição como teste (modo 1):
        # new_competition = Competition()
        # new_competition.competition = 'teste'
        # new_competition.save()

        # Criando nova competição como teste (modo 2):
        # new_competition = Competition.objects.create(
        #     competition='Isso foi criado via objects.create')

        # Atualizando uma competição:
        # new_competition = Competition.objects.create(
        #     competition='Isso foi criado via objects.create para ser alterado.')  # noqa: E501
        # print(
        #     f'Imprimindo para verificar a informação antes de ser alterada: {new_competition}')  # noqa: E501
        # new_competition.competition = 'TEXTO ALTERADO!!!!!!!!'
        # new_competition.save()

        # Buscando uma competição:
        # outra_competition = Competition()
        # outra_competition.competition = 'Outra competição!!!'
        # outra_competition.save()
        # competicao = Competition.objects.get(id=19)
        # print(f'COMPETIÇÃO ENCONTRADA: {competicao}')

        # Deletando do banco:
        # outra_competition2 = Competition()
        # outra_competition2.competition = 'Acabou de criar e será deletado.'
        # outra_competition2.save()
        # print(outra_competition2)
        # outra_competition2.delete()
        # print('Foi deletado!')
        # print(outra_competition2)

        # Filtrando e deletando uma competição: (importante usar o filter no lugar do get pois não apresenta erro)  # noqa: E501
        # competition_filter = Competition.objects.filter(id=6)
        # print(f'ENCONTROU: {competition_filter}')
        # competition_filter.first()
        # competition_filter.first().delete()

        getAthletes = CreateCompetition.objects.filter().order_by('-id')

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
                          'if_competition_ok': True,
                          'athletes': getAthletes,
                          'form': form
                      })
