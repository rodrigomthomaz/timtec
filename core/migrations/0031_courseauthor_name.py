# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_lesson_custom_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['lesson', 'position'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.AlterField(
            model_name='courseauthor',
            name='name',
            field=models.TextField(max_length=100, null=True, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='coursecertification',
            name='course_total_units',
            field=models.IntegerField(verbose_name='Total topics', blank=True),
        ),
        migrations.AlterField(
            model_name='studentprogress',
            name='unit',
            field=models.ForeignKey(related_name='progress', verbose_name='Topic', to='core.Unit'),
        ),
    ]
