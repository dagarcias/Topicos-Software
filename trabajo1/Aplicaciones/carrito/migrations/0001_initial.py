# Generated by Django 4.2.4 on 2023-08-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('codigo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('tipoDePrenda', models.CharField(max_length=40)),
            ],
        ),
    ]
