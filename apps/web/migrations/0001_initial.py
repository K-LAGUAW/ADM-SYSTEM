# Generated by Django 4.2.20 on 2025-05-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('dni', models.CharField(blank=True, max_length=8, null=True, unique=True, verbose_name='DNI')),
                ('phone', models.CharField(max_length=10, verbose_name='Celular')),
                ('province', models.CharField(max_length=100, verbose_name='Provincia')),
                ('locality', models.CharField(blank=True, max_length=100, null=True, verbose_name='Localidad')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
    ]
