from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import CreateForm
from .models import CreateCompetition


def create_competition(request):
    create_form_data = request.session.get('create_form_data', None)
    form = CreateForm(create_form_data)
    name_athlete = form['name_athlete']
    print(f'FORM: {name_athlete}')

    getAthletes = CreateCompetition.objects.filter().order_by('-id')

    return render(request, 'create_competition/pages/home.html',
                  context={
                      'if_competition_ok': True,
                      'athletes': getAthletes,
                      'form': form
                  })


def created_competition(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    # Criando session
    request.session['create_form_data'] = POST
    form = CreateForm(POST)

    if form.is_valid():
        data = form.save()  # noqa: F841
        messages.success(request, 'Cadastro realizado com sucesso!')

        del(request.session['create_form_data'])

    return redirect('create_competition:home')
