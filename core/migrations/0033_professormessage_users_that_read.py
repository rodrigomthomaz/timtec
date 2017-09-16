# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_video_name_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professormessage',
            name='users_that_read',
            field=models.ManyToManyField(related_name='read_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='youtube_id',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
