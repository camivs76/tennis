# Generated by Django 3.1 on 2024-08-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='fechap',
            field=models.FloatField(verbose_name='Fecha de Pago'),
        ),
    ]