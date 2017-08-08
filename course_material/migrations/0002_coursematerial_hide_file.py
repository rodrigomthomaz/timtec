# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Hide'),
        ),
        migrations.AlterField(
            model_name='coursematerial',
            name='text',
            field=models.TextField(verbose_name='Question', blank=True),
        ),
    ]
