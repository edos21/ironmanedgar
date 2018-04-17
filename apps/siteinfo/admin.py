from django.contrib import admin
from .models import Section, SiteInfo
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(SiteInfo)
class SiteinfoAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Site Info'), {'fields': ('name', 'logo',)}),
        (_('Contact Info'), {'fields': ('email', 'phone', 'address', 'facebook', 'twitter')}),
        (_('Active Sections'), {'fields': ('sections',)}),
    )
    filter_horizontal = ('sections',)