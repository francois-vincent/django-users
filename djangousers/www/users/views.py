# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from djangousers.utils import get_last_path

from . import forms


def login_post(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.info(request, _(u'Welcome back %s !') % user)
            else:
                messages.warning(request, _(u"Oops, this user is not active !"))
        else:
            messages.warning(request, _(u"Oops, unknown username or wrong password !"))
    return redirect(get_last_path(request))


def login_view(request):
    return render(request, 'users/login.html', {'autologin': 'true'})


def logout_view(request):
    logout(request)
    return redirect(get_last_path(request))


def create_account(request):
    if request.user.is_authenticated():
        messages.info(request, _(u'%s, you must be deconnected to create a new account' % request.user))
        return redirect('/')
    post = request.POST
    form = forms.UserForm(post or None)
    password_error = None
    if post:
        password = post.get('password')
        if len(password) < 4:
            password_error = _(u'Password must be at least 4 char long.')
        elif password != post.get('password2'):
            password_error = _(u'Passwords are different, please retype.')
        elif form.is_valid():
            form.save()
            username = post['username']
            password = post['password']
            user = form.instance
            if user:
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, _(u'New user %s successfully created !') % user)
                return redirect(get_last_path(request))
            else:
                messages.warning(request, _(u'User creation problem, please retry.'))
    ctxt = {'form': form, 'password_error': password_error}
    return render(request, 'users/create_user.html', ctxt)


def edit_account(request):
    if not request.user.is_authenticated():
        messages.info(request, _(u'You must be connected to edit your account'))
        return redirect('/')
    user = request.user
    post = request.POST
    form = forms.UserForm(post or None, instance=user)
    if not settings.USERS_CAN_MODIFY_USERNAME:
        form.fields['username'].widget.attrs['readonly'] = True
    if not settings.USERS_CAN_MODIFY_EMAIL:
        form.fields['email'].widget.attrs['readonly'] = True
    if post and form.is_valid():
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        try:
            user.save()
            messages.success(request, _(u'User %s successfully modified !') % user)
            return redirect(get_last_path(request))
        except Exception as e:
            messages.warning(request, _(u'User modification problem: %s' % e))
    return render(request, 'users/edit_user.html', {'form': form})


def change_password(request):
    user = request.user
    post = request.POST
    password_error = None
    if post:
        password = post.get('password')
        if len(password) < 4:
            password_error = _(u'Password must be at least 4 char long.')
        elif password != post.get('password2'):
            password_error = _(u'Passwords are different, please retype.')
        else:
            user.set_password(password)
            user.save()
            messages.success(request, _(u'Password successfully modified !'))
            return redirect(get_last_path(request))
    return render(request, 'users/change_password.html', {'password_error': password_error})
