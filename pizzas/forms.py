from django import forms

from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
