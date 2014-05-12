# -*- coding: utf-8 -*-

from django.conf import settings

from djangousers.utils import get_last_path


def users_can_do(request):
    return {
        'USERS_CAN_CREATE_USER': settings.USERS_CAN_CREATE_USER,
    }


def last_page(request):
    return {
        'LAST_TRUE_PAGE': get_last_path(request),
    }
