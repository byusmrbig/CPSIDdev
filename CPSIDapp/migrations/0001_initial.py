# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectImpact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DirectImpact', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GroupName', models.CharField(max_length=1024)),
                ('Email', models.CharField(max_length=1024)),
                ('GroupAddress', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Immediacy', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=1024)),
                ('RecoveryTime', models.CharField(max_length=1024)),
                ('financialImpact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=1024)),
                ('Description', models.TextField(max_length=9064)),
                ('ReviewStatus', models.CharField(max_length=1024)),
                ('User', models.IntegerField()),
                ('Group', models.ForeignKey(to='CPSIDapp.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='IncidentChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DateOfChange', models.DateTimeField()),
                ('User', models.IntegerField()),
                ('ChangesMade', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='IndirectImpact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('IndirectImpact', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='Means',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='SeverityOfImpact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Severity', models.CharField(max_length=255)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(max_length=1024)),
                ('Details', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FirstName', models.CharField(max_length=1024)),
                ('LastName', models.CharField(max_length=1024)),
                ('Position', models.CharField(max_length=1024)),
                ('Group', models.ForeignKey(to='CPSIDapp.Groups')),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Type', models.CharField(max_length=1024)),
                ('Details', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='VictimSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Sector', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=1024)),
                ('IncidentID', models.ForeignKey(to='CPSIDapp.Incident')),
            ],
        ),
        migrations.AddField(
            model_name='impact',
            name='IncidentID',
            field=models.ForeignKey(to='CPSIDapp.Incident'),
        ),
        migrations.AddField(
            model_name='directimpact',
            name='IncidentID',
            field=models.ForeignKey(to='CPSIDapp.Incident'),
        ),
    ]
