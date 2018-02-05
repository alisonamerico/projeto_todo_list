from django import forms


class TodoForm(forms.Form):

    PRIORITY_CHOICES = [
      ('Baixa', 'Baixa'),
      ('Normal', 'Normal'),
      ('Alta', 'Alta'),
      ]

    priority = forms.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Normal')
    completed = forms.BooleanField(required=False)
