from django import forms

from .models import CreateCompetition

# from django.contrib.auth.models import User


class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateCompetition
        fields = '__all__'

        labels = {
            'name_athlete': 'Nome:',
            'age_athlete': 'Idade:',
            'height_athlete': 'Altura:',
            'weight_athlete': 'Peso:',
            'name_competition': 'Modalidade:',
            'place_competition': 'Local:'
        }

        help_texts = {
            'name_competition': 'Escolha a sua modalidade.'
        }

        error_messages = {
            'name_athlete': {
                'required': 'Digite um nome válido.'
            },
            'age_athlete': {
                'required': 'Digite uma idade válida.'
            },
            'height_athlete': {
                'required':  'Digite uma altura válida.'
            },
            'weight_athlete': {
                'required':  'Digite um peso válido.'
            },
            'name_competition': {
                'required':  'Escolha uma modalidade.'
            }
        }

        widgets = {
            'name_athlete': forms.TextInput(attrs={
                'placeholder': 'Digite o seu nome',
                'class': 'form-control',
                'type': 'text'
            }),
            'age_athlete': forms.TextInput(attrs={
                'placeholder': 'Digite a sua idade',
                'class': 'form-control',
                'type': 'number'
            }),
            'height_athlete': forms.TextInput(attrs={
                'placeholder': 'Digite a sua altura',
                'class': 'form-control',
                'type': 'number'
            }),
            'weight_athlete': forms.TextInput(attrs={
                'placeholder': 'Digite o seu peso',
                'class': 'form-control',
                'type': 'number'
            }),
            'name_competition': forms.Select(attrs={
                'class': 'form-control custom-select selectpicker'
            }),
            'place_competition': forms.Select(attrs={
                'class': 'form-control custom-select selectpicker'
            })
        }
