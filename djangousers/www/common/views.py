# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from djangousers.utils import mark_path

@mark_path
def home(request):
    return render(request, 'common/home.html')


@mark_path
def page1(request):
    return render(request, 'common/page1.html')


@mark_path
def page2(request):
    return render(request, 'common/page2.html')


@mark_path
def page3(request):
    return render(request, 'common/page3.html')


@mark_path
def page4(request):
    return render(request, 'common/page4.html')


@mark_path
@login_required(login_url=reverse_lazy('users:login_required'))
def page5(request):
    return render(request, 'common/page5.html')
