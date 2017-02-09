# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20170201_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='content',
            field=models.TextField(null=True, verbose_name='Content', blank=True),
        ),
    ]
