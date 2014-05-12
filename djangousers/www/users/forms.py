# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import models as auth_models


class UserForm(forms.ModelForm):

    class Meta:
        model = auth_models.User
        fields = ('username', 'first_name', 'last_name', 'email')
