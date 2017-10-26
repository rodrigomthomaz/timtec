# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20170419_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='positive_feedback',
        ),
        migrations.AlterField(
            model_name='activity',
            name='negative_feedback',
            field=models.TextField(null=True, verbose_name='Negative Feedback', blank=True),
        ),
    ]
