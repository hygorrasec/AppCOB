from django import forms

from .models import CreateCompetition

# from django.contrib.auth.models import User


class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateCompetition
        fields = '__all__'
