# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _


TITLE_CHOICES = (
    ('MR', _(u'Mr.')),
    ('MRS', _(u'Mrs.')),
    ('MS', _(u'Ms.')),
)


class UserProfile(auth_models.User):
    title = models.CharField(_(u'title'), max_length=3, choices=TITLE_CHOICES, blank=True)
    birthdate = models.DateField(_(u'birthdate'), blank=True)
    date_left = models.DateTimeField(_(u'date left'), blank=True)

    class Meta:
        verbose_name = _(u"user profile")
        verbose_name_plural = _(u"user profiles")

    def __unicode__(self):
        return self.user.username
