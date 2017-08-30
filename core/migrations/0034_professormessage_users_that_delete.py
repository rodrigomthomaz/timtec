# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0033_professormessage_users_that_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='professormessage',
            name='users_that_delete',
            field=models.ManyToManyField(related_name='delete_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
