# Generated by Django 3.2.12 on 2022-12-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_auto_20221214_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.CharField(choices=[('First owner', 'First owner'), ('Second owner', 'Second owner'), ('Third owner', 'Third owner'), ('Fourth owner', 'Fourth owner'), ('Fifth owner', 'Fifth owner')], max_length=100),
        ),
    ]
