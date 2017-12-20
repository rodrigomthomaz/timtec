# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_message_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='professormessage',
            name='is_system_message',
            field=models.BooleanField(default=False, verbose_name='System Messsage'),
        ),
    ]
