import json

import requests
import jwt

from timtec import settings


class IntegrationUtils():

    @staticmethod
    def getNNEProfile(jwtToken):
        r = requests.get(settings.INTEGRATION_PROFILE_URL, headers={'Authorization': 'Bearer ' + jwtToken})
        return r.json()