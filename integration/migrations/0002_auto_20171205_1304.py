# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrationdata',
            name='num_stories_pending',
            field=models.CharField(max_length=10, null=True, verbose_name='Stories Pending', blank=True),
        ),
        migrations.AddField(
            model_name='integrationdata',
            name='num_stories_published',
            field=models.CharField(max_length=10, null=True, verbose_name='Stories Publised', blank=True),
        ),
        migrations.AddField(
            model_name='integrationdata',
            name='num_stories_started',
            field=models.CharField(max_length=10, null=True, verbose_name='Stories Started', blank=True),
        ),
        migrations.AddField(
            model_name='integrationdata',
            name='num_stories_total',
            field=models.CharField(max_length=10, null=True, verbose_name='Stories Total', blank=True),
        ),
    ]
