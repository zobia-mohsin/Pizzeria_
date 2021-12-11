from django.shortcuts import render
from .models import Pizza
# Create your views here.


def index(request):
    return render(request, 'Pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date')

    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings_set.order_by('-date_added')
    comments = pizza.comment_set.order_by('-date_added')

    context = {'pizza': pizza, 'toppings': toppings, 'comments': comments}
    return render(request, 'pizzas/pizza.html', context)
