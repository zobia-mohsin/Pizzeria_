# Generated by Django 3.2.10 on 2021-12-13 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_pizza_header_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comment'},
        ),
    ]