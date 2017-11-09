import requests
import jwt

from timtec import settings


class IntegrationUtils():

    @staticmethod
    def getNNEProfile(subscription_id):

        jwtToken = jwt.encode({'sub': subscription_id}, settings.INTEGRATION_JWT_SECRET, 'HS256')

        r = requests.get(settings.INTEGRATION_PROFILE_URL, headers={'Authorization': 'Bearer ' + jwtToken})
        return r.json()
