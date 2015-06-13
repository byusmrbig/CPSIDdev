# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPSIDapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directimpact',
            options={'verbose_name_plural': 'DirectImpacts'},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='impact',
            options={'verbose_name_plural': 'Impacts'},
        ),
        migrations.AlterModelOptions(
            name='incident',
            options={'verbose_name_plural': 'Incidents'},
        ),
        migrations.AlterModelOptions(
            name='incidentchange',
            options={'verbose_name_plural': 'IncidentChanges'},
        ),
        migrations.AlterModelOptions(
            name='indirectimpact',
            options={'verbose_name_plural': 'IndirectImpacts'},
        ),
        migrations.AlterModelOptions(
            name='means',
            options={'verbose_name_plural': 'Means'},
        ),
        migrations.AlterModelOptions(
            name='severityofimpact',
            options={'verbose_name_plural': 'SeverityOfImpacts'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name_plural': 'Sources'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='victim',
            options={'verbose_name_plural': 'Victims'},
        ),
        migrations.AlterModelOptions(
            name='victimsector',
            options={'verbose_name_plural': 'VictimSectors'},
        ),
    ]
