# Generated by Django 2.1.1 on 2018-10-13 14:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coordenador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('data', models.DateField(default=datetime.datetime(2018, 10, 13, 11, 16, 5, 711347))),
                ('status', models.CharField(default='ABERTA', max_length=7)),
                ('planoDeEnsino', models.TextField()),
                ('cargaHoraria', models.IntegerField()),
                ('competencias', models.CharField(max_length=30)),
                ('habilidade', models.CharField(max_length=30)),
                ('ementa', models.CharField(max_length=30)),
                ('conteudoProgramatico', models.CharField(max_length=30)),
                ('bibliografiaBasica', models.CharField(max_length=30)),
                ('bibliografiaComplementar', models.CharField(max_length=30)),
                ('percentualPatrico', models.IntegerField()),
                ('percentualTeorico', models.IntegerField()),
                ('id_coordenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordenador.Coordenador')),
            ],
        ),
    ]
