# -*- coding: utf-8 -*-

from functools import wraps
import urlparse


def get_last_path(request):
    if hasattr(request, 'session') and 'last_path' in request.session:
        return request.session['last_path']
    referer, target = request.META.get('HTTP_REFERER'), None
    if referer:
        query = urlparse.urlparse(referer).query
        target = urlparse.parse_qs(query).get('next')
    if target:
        target = target[0]
    if not target:
        target = request.REQUEST.get('next')
    if not target:
        target = referer
    if not target or target.endswith(request.path):
        target = '/'
    return target


def mark_path(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        request = args[0]
        if hasattr(request, 'session'):
            request.session['last_path'] = request.path
        return func(*args, **kwargs)
    return wrapped
