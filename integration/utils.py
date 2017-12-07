import requests
import jwt

from django.conf import settings
from django.contrib.auth import get_user_model
from .models import IntegrationData


class IntegrationUtils():

    @staticmethod
    def getNNEProfile(subscription_id):

        jwtToken = jwt.encode({'sub': subscription_id}, settings.INTEGRATION_JWT_SECRET, 'HS256')

        r = requests.get(settings.INTEGRATION_PROFILE_URL, headers={'Authorization': 'Bearer ' + jwtToken})
        return r.json()


def load_profile_all():

    if not hasattr(settings, 'INTEGRATION_PROFILE_ALL_EDITIONS') or not settings.INTEGRATION_PROFILE_ALL_EDITIONS:
        return

    for edition in settings.INTEGRATION_PROFILE_ALL_EDITIONS:

        params = {
            'edition_id': edition,
            'key': settings.INTEGRATION_PROFILE_ALL_SECRET
        }

        r = requests.get(settings.INTEGRATION_PROFILE_ALL_URL, params=params)
        user_model = get_user_model()
        if r.ok:
            for profile in r.json().get('profiles'):
                try:
                    user = user_model.objects.get(id=profile.get('sub_id'))
                    print "Added"
                except user_model.DoesNotExist:
                    print "Skipped"
                    continue

                save_integration_data(user, profile)


def save_integration_data(user, json):

    if not hasattr(user, 'integration_data'):
        user.integration_data = IntegrationData()

    user.integration_data.city = json.get('city').get('name')
    user.integration_data.edition = json.get('edition')
    user.integration_data.formation_type = json.get('formation_type')
    user.integration_data.participation_type = json.get('participation_type')
    user.integration_data.region = json.get('region').get('name')
    user.integration_data.rf = json.get('rf')
    user.integration_data.school = json.get('school').get('name')
    user.integration_data.track = json.get('track').get('name')
    user.integration_data.num_stories_total = json.get('num_stories_total')
    user.integration_data.num_stories_started = json.get('num_stories_started')
    user.integration_data.num_stories_pending = json.get('num_stories_pending')
    user.integration_data.num_stories_published = json.get('num_stories_published')

    user.integration_data.save()
