# Generated by Django 4.0.4 on 2022-06-01 03:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_alter_aluno_cpf_alter_aluno_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999999)]),
        ),
    ]
