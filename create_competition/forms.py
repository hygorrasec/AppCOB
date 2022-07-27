from django import forms
from django.core.exceptions import ValidationError

from .models import CreateCompetition


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def check_age(age_athlete):
    if int(age_athlete) < 15:
        raise ValidationError((
            'Para participar, você precisa ter 15 anos ou mais.'
        ))
    elif int(age_athlete) > 80:
        raise ValidationError((
            'A idade máxima permitida é 80 anos.'
        ))


def check_height(height_athlete):
    if float(height_athlete) <= 1:
        raise ValidationError((
            'Para participar, você precisa ter mais de 1 metro de altura.'
        ))


class CreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['name_athlete'], 'Digite o seu nome')
        add_placeholder(self.fields['age_athlete'], 'Digite a sua idade')
        add_placeholder(self.fields['height_athlete'], 'Digite a sua altura')
        add_placeholder(self.fields['weight_athlete'], 'Digite o seu peso')
        add_attr(self.fields['name_athlete'], 'class', 'form-control')
        add_attr(self.fields['age_athlete'], 'class', 'form-control')
        add_attr(self.fields['height_athlete'], 'class', 'form-control')
        add_attr(self.fields['weight_athlete'], 'class', 'form-control')
        add_attr(self.fields['name_competition'], 'class',
                 'form-control custom-select selectpicker')
        add_attr(self.fields['place_competition'], 'class',
                 'form-control custom-select selectpicker')

    name_athlete = forms.CharField(
        required=True,
        label='Nome:'
    )
    age_athlete = forms.CharField(
        required=True,
        label='Idade:',
        error_messages={
            'required': 'Digite uma idade válida.'
        },
        widget=forms.TextInput(attrs={
            'type': 'number'
        }),
        validators=[check_age]
    )
    height_athlete = forms.CharField(
        required=True,
        label='Altura:',
        error_messages={
            'required':  'Digite uma altura válida.'
        },
        widget=forms.TextInput(attrs={
            'type': 'number',
            'step': '0.01'
        }),
        validators=[check_height]
    )
    weight_athlete = forms.CharField(
        required=True,
        label='Peso:',
        error_messages={
            'required':  'Digite um peso válido.'
        },
        widget=forms.TextInput(attrs={
            'type': 'number',
            'step': '0.01'
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

    # def clean_name_athlete(self):
    #     data = self.cleaned_data.get('name_athlete')

    #     if 'Hygor' in data:
    #         raise ValidationError(
    #             'Não digite %(value)s no campo Nome',
    #             code='invalid',
    #             params={'value': '"Hygor"'}
    #         )

    #     return data

    def clean(self):
        cleaned_data = super().clean()
        name_athlete = cleaned_data.get('name_athlete')

        if 'Hygor' in name_athlete:
            raise ValidationError({
                'name_athlete': ValidationError(
                    'Não digite %(value)s no campo Nome',
                    code='invalid',
                    params={'value': '"Hygor"'}
                )
            })
