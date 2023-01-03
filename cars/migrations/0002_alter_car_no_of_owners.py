# Generated by Django 3.2.12 on 2022-12-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.IntegerField(choices=[('1', 'First owner'), ('2', 'Second owner'), ('3', 'Third owner'), ('4', 'Fourth owner'), ('5', 'Fifth owner')]),
        ),
    ]
