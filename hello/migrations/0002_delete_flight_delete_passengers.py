# Generated by Django 4.0.2 on 2022-03-07 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Flight',
        ),
        migrations.DeleteModel(
            name='Passengers',
        ),
    ]
