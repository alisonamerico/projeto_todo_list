from django import forms

from .models import Todo


class TodoForms(forms.ModelForm):
    BAIXA = 1
    NORMAL = 2
    ALTA = 3

    PRIORITY_CHOICES = [
      ('BAIXA', 'Baixa'),
      ('NORMAL', 'Normal'),
      ('ALTA', 'Alta'),
      ]

    priority = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=PRIORITY_CHOICES)

    completed = forms.CheckboxInput(widget=forms.CheckboxInput)

    class Meta:
        model = Todo
