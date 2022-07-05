# Generated by Django 3.2 on 2022-06-03 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnexoModel',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('imagen', models.FileField(upload_to='soporte/')),
                ('comentario', models.CharField(max_length=100, null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, db_column='fecha_ingreso', null=True)),
                ('votante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.votantemodel')),
            ],
            options={
                'verbose_name': 'Anexo anexo',
                'verbose_name_plural': 'Anexo usuarios',
                'db_table': 'anexo',
                'managed': True,
            },
        ),
    ]
