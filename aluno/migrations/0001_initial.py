# Generated by Django 4.0.4 on 2022-06-01 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_create', models.DateTimeField(auto_now_add=True)),
                ('at_update', models.DateTimeField(auto_now=True)),
                ('matricula', models.IntegerField(max_length=11)),
                ('cpf', models.IntegerField(max_length=11)),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=80)),
                ('telefone', models.IntegerField(max_length=14)),
            ],
            options={
                'ordering': ['cpf', 'nome', 'matricula', 'email', 'telefone'],
            },
        ),
    ]