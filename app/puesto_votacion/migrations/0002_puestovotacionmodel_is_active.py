# Generated by Django 3.2 on 2022-06-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puesto_votacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puestovotacionmodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
