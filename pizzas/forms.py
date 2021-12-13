from django import forms

from .models import Pizza, Toppings, Comment


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'header_image']
        labels = {'name': ''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class ToppingForm(forms.ModelForm):
    class Meta:
        model = Toppings
        fields = ['name']
        labels = {'name': ''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name': ''}
        #widgets = {'text': forms.Textarea(attrs={'cols': 80})}
