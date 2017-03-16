# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def enroll_user_to_clas(apps, schema_editor):
    """Enroll user to class."""
    return
    CourseStudent = apps.get_model("core", "CourseStudent")
    for cs in CourseStudent.objects.all():

        user_in_class = False
        for class_ in cs.course.class_set.all():
            if class_.students.filter(id=cs.user.id).exists():
                user_in_class = True
                break

        if not user_in_class:
            cs.course.default_class.students.add(cs.user)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_course_welcome_email'),
    ]

    operations = [
        migrations.RunPython(enroll_user_to_clas),
    ]
