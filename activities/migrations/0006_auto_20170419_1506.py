# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20170209_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='unit',
            field=models.ForeignKey(related_name='activities', verbose_name='Topic', blank=True, to='core.Unit', null=True),
        ),
    ]
