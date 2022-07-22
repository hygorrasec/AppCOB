from django import forms

from .models import CreateCompetition


class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateCompetition
        fields = "__all__"
