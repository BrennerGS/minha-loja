# Generated by Django 5.0.6 on 2024-06-30 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='CNPJ_CPF',
            field=models.IntegerField(unique=True),
        ),
    ]
