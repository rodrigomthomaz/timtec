from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class IntegrationData(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='integration_data', null=True, blank=True)
    city = models.CharField(_('City'), max_length=100, null=True, blank=True)
    edition = models.CharField(_('Edition'), max_length=100, null=True, blank=True)
    formation_type = models.CharField(_('Formation Type'), max_length=100, null=True, blank=True)
    participation_type = models.CharField(_('Participation Type'), max_length=100, null=True, blank=True)
    region = models.CharField(_('Region'), max_length=100, null=True, blank=True)
    rf = models.CharField(_('RF'), max_length=100, null=True, blank=True)
    school = models.CharField(_('School'), max_length=100, null=True, blank=True)
    track = models.CharField(_('Track'), max_length=100, null=True, blank=True)
    num_stories_total = models.CharField(_('Stories Total'), max_length=10, null=True, blank=True)
    num_stories_started = models.CharField(_('Stories Started'), max_length=10, null=True, blank=True)
    num_stories_pending = models.CharField(_('Stories Pending'), max_length=10, null=True, blank=True)
    num_stories_published = models.CharField(_('Stories Publised'), max_length=10, null=True, blank=True)
