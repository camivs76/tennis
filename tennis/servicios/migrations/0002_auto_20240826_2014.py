# Generated by Django 3.1 on 2024-08-26 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contratacion',
            fields=[
                ('idContratacion', models.AutoField(db_column='idContratacion', primary_key=True, serialize=False)),
                ('fecha', models.IntegerField(verbose_name='fecha')),
                ('nomContratante', models.TextField(max_length=25, verbose_name='nomContratante')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.AutoField(db_column='Código del Servicio', primary_key=True, serialize=False)),
                ('descripcion', models.TextField(verbose_name='Descripción del Servicio')),
                ('costo', models.FloatField(max_length=50, verbose_name='Costo del Servicio')),
            ],
        ),
        migrations.DeleteModel(
            name='Socio',
        ),
        migrations.AddField(
            model_name='contratacion',
            name='idServicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.servicio', verbose_name='idServicio'),
        ),
    ]