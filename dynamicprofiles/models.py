from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('user'))

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.user.username


class ProfileDataGroup(models.Model):
    name = models.CharField(max_length=60, blank=True, unique=True)

    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ProfileDataField(models.Model):
    name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=255, blank=True)

    choices = models.CharField(max_length=512, blank=True)

    TYPE_OPTIONS = (('text', 'Text'),
                    ('longtext', 'Long Text'),
                    ('choice', 'Choice'))
    field_type = models.CharField(max_length=30, choices=TYPE_OPTIONS)

    order = models.PositiveIntegerField()

    group = models.ForeignKey(ProfileDataGroup, null=False)

    class Meta:
        unique_together = (('name', 'group'))
        
    def __str__(self):
        return self.group.name + ': ' + self.name


class ProfileData(models.Model):
    field = models.ForeignKey(ProfileDataField, null=False)
    profile = models.ForeignKey(Profile, null=False)

    data = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "%s, %s" % (self.profile, self.field)

    def value(self):
        if self.field.field_type == 'longtext':
            return self.profiletextdata.text_data
        else:
            return self.data

class ProfileTextData(ProfileData):
    text_data = models.TextField(blank=True)
