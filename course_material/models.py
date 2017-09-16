# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class CourseMaterial(models.Model):
    course = models.OneToOneField('core.Course', related_name='course_material', verbose_name=_('Course Materials'))
    text = models.TextField(_('Question'), blank=True)

    class Meta:
        unique_together = ("id", "course")

    def __unicode__(self):
        return self.course.name


def get_upload_path(instance, filename):
    file_split = filename.split(".", 2)
    if len(file_split) == 2:
        filename, fileextension = file_split
    else:
        filename = file_split[0]
        fileextension = '.'

    filename = slugify(filename.split("/", 2)[-1])
    return '{0}/course_materials/{1}.{2}'.format(instance.course_material.course.slug, filename, fileextension)


class File(models.Model):
    file = models.FileField(upload_to=get_upload_path)
    course_material = models.ForeignKey(CourseMaterial, related_name='files', verbose_name=_('Files'))
    hide = models.BooleanField(_('Hide'), default=False)
