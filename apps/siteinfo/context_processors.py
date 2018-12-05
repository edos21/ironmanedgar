# -*- coding: utf-8 -*-
from siteinfo.models import SiteInfo

def site_info(request):
    site = SiteInfo.objects.last()
    if site is None:
        sections = []
    else:
        sections = [s.name for s in site.sections.all()]
    return {
            'site':site,
            'sections':sections,
        }
