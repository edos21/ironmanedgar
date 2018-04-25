# -*- coding: utf-8 -*-
from siteinfo.models import Section, SiteInfo

def site_info(request):
    site = SiteInfo.objects.last()
    return {
            'site':site,
        }