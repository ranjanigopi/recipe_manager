# Generated by Django 3.1.3 on 2020-11-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=75)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
