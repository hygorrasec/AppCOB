from django.shortcuts import redirect, render

from .forms import CreateForm
from .models import CreateCompetition


def create_competition(request):
    print(f'MÉTODO: {request.method}')
    if request.method == 'POST':
        print('olá')
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateForm()
        # print(f'FORM: {form}')
        athletes = CreateCompetition.objects.all().order_by('-created_at')
        print(f'ATLETA: {athletes}')
        return render(request, 'create_competition/home.html', {'athletes': athletes, 'form': form})
