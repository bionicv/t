# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('severity', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('length_open', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('up_vote', models.IntegerField()),
                ('down_vote', models.IntegerField()),
                ('emergency_level', models.ForeignKey(to='incidents.EmergencyLevel')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_field', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='incident_type',
            field=models.ForeignKey(to='incidents.IncidentType'),
        ),
        migrations.AddField(
            model_name='incident',
            name='status',
            field=models.ForeignKey(to='incidents.Status'),
        ),
    ]
