from django import forms

from .models import CreateCompetition


class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateCompetition
        fields = ('name_competition', 'place_competition', 'name_athlete',
                  'age_athlete', 'height_athlete', 'weight_athlete')
