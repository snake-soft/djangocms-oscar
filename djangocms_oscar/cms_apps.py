# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from .menu import CategoriesMenu
from django.urls.conf import path, include
from django.apps.registry import apps


class OscarApp(CMSApp):
    """
    Allows "mounting" the oscar shop and all of its urls to a specific CMS page.
    e.g at "/shop/"
    """
    name = _("Oscar")
    #===========================================================================
    # urls = [
    #     patterns('', *application.urls[0])
    # ]
    #===========================================================================
    menus = [CategoriesMenu]

    def get_urls(self, page=None, language=None, **kwargs):
        return path('', include(apps.get_app_config('oscar').urls[0])),

apphook_pool.register(OscarApp)
