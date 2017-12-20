# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0034_professormessage_users_that_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.AddField(
            model_name='messageanswer',
            name='message',
            field=models.ForeignKey(related_name='answers', verbose_name='Message', to='core.ProfessorMessage'),
        ),
        migrations.AddField(
            model_name='messageanswer',
            name='user',
            field=models.ForeignKey(related_name='message_answers', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
