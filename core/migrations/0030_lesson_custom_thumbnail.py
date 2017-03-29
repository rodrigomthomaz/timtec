# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20170209_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='custom_thumbnail',
            field=models.ImageField(upload_to=core.utils.HashName(b'lesson_thumbnails', b'name'), null=True, verbose_name='Thumbnail', blank=True),
        ),
    ]
