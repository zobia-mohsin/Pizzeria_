from django import forms

from .models import Pizza


class PizzaForm(form.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}
