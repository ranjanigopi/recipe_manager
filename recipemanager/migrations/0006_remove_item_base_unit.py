# Generated by Django 3.1.3 on 2020-12-02 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipemanager', '0005_auto_20201202_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='base_unit',
        ),
    ]
