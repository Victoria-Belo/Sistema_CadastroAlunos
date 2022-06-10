# Generated by Django 4.0.4 on 2022-06-01 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.IntegerField(max_length=11, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(max_length=14, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999999)]),
        ),
    ]