from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.conf import settings
from apps.main import MultiSelectField

class SiteInfo(models.Model):
    BLOCK_CHOICES = [b[:2] for b in settings.ARTICLE_BLOCKS]

    name = models.CharField(_("Name"), max_length=50)
    logo = models.FileField(_('File'), upload_to='articles_files/', null=True, blank=True)
    #Contact Info
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), null=True, blank=True)
    address = models.TextField(_("Address"), null=True, blank=True)
    #Social Info
    facebook = models.URLField(_("Facebook"), null=True, blank=True)
    twitter = models.URLField(_("Facebook"), null=True, blank=True)
    # Fields
    block = MultiSelectField(_('Block'), max_length=1000, choices=BLOCK_CHOICES)
