# -*- coding: utf-8 -*-
from django.conf import settings
from .utils import IntegrationUtils


def load_banner(request):
    context = {}
    if request.user.is_authenticated() and hasattr(settings, 'LOAD_BANNER_FORMATIONS') and settings.LOAD_BANNER_FORMATIONS:
        u = IntegrationUtils.getNNEProfile(request.user.id)
        try:
            if u.get('profile', {}).get('current', {}).get('formation', {}).get('id', {}) in settings.LOAD_BANNER_FORMATIONS:
                context = {
                    'load_banner_nne': True
                }
        except:
            pass

    return context
