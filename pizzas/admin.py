from django.contrib import admin

# Register your models here.
from .models import Pizza, Toppings, Comment

admin.site.register(Pizza)
admin.site.register(Toppings)
admin.site.register(Comment)
