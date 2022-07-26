from tkinter import Widget

from django import forms

from .models import CreateCompetition


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


class CreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name_athlete'], 'Digite o seu nome')
        add_placeholder(self.fields['age_athlete'], 'Digite a sua idade')
        add_placeholder(self.fields['height_athlete'], 'Digite a sua altura')
        add_placeholder(self.fields['weight_athlete'], 'Digite o seu peso')

    name_athlete = forms.CharField(
        required=True,
        label='Nome:',
        error_messages={
            'required': 'Digite um nome válido.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'text'
        })
    )
    age_athlete = forms.CharField(
        required=True,
        label='Idade:',
        error_messages={
            'required': 'Digite uma idade válida.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'number'
        })
    )
    height_athlete = forms.CharField(
        required=True,
        label='Altura:',
        error_messages={
            'required':  'Digite uma altura válida.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'number'
        })
    )
    weight_athlete = forms.CharField(
        required=True,
        label='Peso:',
        error_messages={
            'required':  'Digite um peso válido.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'number'
        })
    )

    class Meta:
        model = CreateCompetition
        fields = '__all__'

        labels = {
            'name_competition': 'Modalidade:',
            'place_competition': 'Local:'
        }

        help_texts = {
            'name_competition': 'Escolha a sua modalidade.'
        }

        error_messages = {
            'name_competition': {
                'required':  'Escolha uma modalidade.'
            }
        }

        widgets = {
            'name_competition': forms.Select(attrs={
                'class': 'form-control custom-select selectpicker'
            }),
            'place_competition': forms.Select(attrs={
                'class': 'form-control custom-select selectpicker'
            })
        }
