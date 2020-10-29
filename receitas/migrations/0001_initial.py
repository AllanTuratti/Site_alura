# Generated by Django 3.1.1 on 2020-09-29 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=100)),
                ('ingrediente', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField(max_length=100)),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('date_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
