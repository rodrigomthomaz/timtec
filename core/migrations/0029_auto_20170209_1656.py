# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_course_total_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_hours',
            field=models.IntegerField(default=0, null=True, verbose_name='Total hours'),
        ),
    ]
