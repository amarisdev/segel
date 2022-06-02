# Generated by Django 3.2 on 2022-06-02 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divipol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZonaVotacionModel',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('numero', models.IntegerField(blank=True, db_column='numero', null=True, unique=True)),
                ('codigo', models.CharField(blank=True, db_column='codigo', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=20, null=True)),
                ('divipol', models.ForeignKey(db_column='divipol', on_delete=django.db.models.deletion.CASCADE, to='divipol.divipolmodel')),
            ],
            options={
                'verbose_name': 'zona votacion',
                'verbose_name_plural': 'zona votaciones',
                'db_table': 'zona_votacion',
                'managed': True,
            },
        ),
    ]