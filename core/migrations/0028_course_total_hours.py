# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_unit_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='total_hours',
            field=models.IntegerField(default=0, verbose_name='Total hours'),
        ),
    ]
