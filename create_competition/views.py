from django.shortcuts import redirect, render

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
            athletes = CreateCompetition.objects.all().order_by('-created_at')
            return render(request, 'create_competition/home.html', {'athletes': athletes, 'form': form})
            # return redirect('/')
        else:
            print('APRESENTOU UM ERRO!')

    else:
        form = CreateForm()
        # print(f'FORM: {form}')
        athletes = CreateCompetition.objects.all().order_by('-created_at')
        print(f'ATLETA: {athletes}')
        return render(request, 'create_competition/home.html', {'athletes': athletes, 'form': form})
