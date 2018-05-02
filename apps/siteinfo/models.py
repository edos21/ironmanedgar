from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class  Section(models.Model):
    name = models.CharField(_("Section Name"), max_length=50)

    def __str__(self):
        return self.name


class SiteInfo(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    logo = models.FileField(_('Logo'), upload_to='articles_files/', null=True, blank=True)
    #Contact Info
    email = models.EmailField(_("Email"), help_text="required for contact form")
    phone = models.CharField(_("Phone"), max_length=20, null=True, blank=True)
    address = models.TextField(_("Address"), null=True, blank=True)
    #Social Info
    facebook = models.URLField(_("Facebook"), null=True, blank=True)
    twitter = models.URLField(_("Twitter"), null=True, blank=True)
    # Page Sections
    sections =  models.ManyToManyField(Section, verbose_name=_("Sections"), help_text="at least 1 section is required")

    def __str__(self):
        return self.name