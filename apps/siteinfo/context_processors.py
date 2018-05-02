# -*- coding: utf-8 -*-
from siteinfo.models import SiteInfo

def site_info(request):
    site = SiteInfo.objects.last()
    sections = [s.name for s in site.sections.all()]
    return {
            'site':site,
            'sections':sections,
        }