# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-29 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=40, null=True)),
                ('document_number', models.CharField(max_length=8)),
                ('is_member', models.BooleanField(default=False)),
                ('is_banned', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('departure_time', models.DateTimeField(null=True)),
                ('amount', models.FloatField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=8)),
                ('is_exonerated', models.BooleanField(default=False)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.Client')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('payment_per_night', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tipos de vehiculo',
                'verbose_name_plural': 'Tipos de vehiculo',
            },
        ),
        migrations.CreateModel(
            name='Watchman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Vigilante',
                'verbose_name_plural': 'Vigilantes',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.VehicleType'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.Vehicle'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='watchman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.Watchman'),
        ),
    ]
