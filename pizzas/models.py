from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1. py manage.py makemigrations
# 2. py manage.py migrate
# 3. register - admin.py


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    # to have the title of Toppings say Toppings not Toppings
    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.name
