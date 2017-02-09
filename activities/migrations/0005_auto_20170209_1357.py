# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='comment',
            field=models.TextField(null=True, verbose_name='Comment', blank=True),
        ),
    ]
