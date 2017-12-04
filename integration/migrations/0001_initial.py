# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IntegrationData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name='City', blank=True)),
                ('edition', models.CharField(max_length=100, null=True, verbose_name='Edition', blank=True)),
                ('formation_type', models.CharField(max_length=100, null=True, verbose_name='Formation Type', blank=True)),
                ('participation_type', models.CharField(max_length=100, null=True, verbose_name='Participation Type', blank=True)),
                ('region', models.CharField(max_length=100, null=True, verbose_name='Region', blank=True)),
                ('rf', models.CharField(max_length=100, null=True, verbose_name='RF', blank=True)),
                ('school', models.CharField(max_length=100, null=True, verbose_name='School', blank=True)),
                ('track', models.CharField(max_length=100, null=True, verbose_name='Track', blank=True)),
                ('user', models.OneToOneField(related_name='integration_data', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
