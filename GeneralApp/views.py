# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.deprecation import RemovedInDjango21Warning
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render
from .forms import LoginForm, UserForm
from django.template import loader
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import resolve_url
from django.views.decorators.cache import never_cache
from ProfileApp.models import Profile


# Create your views here.

class LoginFormView(View):
    form_class = LoginForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(None)
        # cleaned (normalized) data

        context = ""
        username = request.POST['username']
        password = request.POST['password']

        # returns User objects if credentials are correct
        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/dashboard')
            else:
                context = "User is banned"
        else:
            context = "Incorrect username or password"

        return render(request, 'GeneralApp/login.html', {'form': form, 'context': context})


class UserFormView(View):
    form_class = UserForm
    context = ""

    def get(self, request):
        form = self.form_class(None)
        context = ""
        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})

    def post(self, request):
        form = self.form_class(request.POST)
        context = ""

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username1 = form.cleaned_data['username1']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 != password2:
                context = "Passwords do not match."
                return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})
            user.set_password(password1)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username1, password=password1)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    context = "Existing user is banned."

        else:
            context = "Please select a unique username."

        return render(request, 'GeneralApp/registration.html', {'form': form, 'context': context})


'''def tnc(request):
    template = loader.get_template('GeneralApp/tnc.html')
    return HttpResponse(template.render(request))'''

def redirect_to_dashboard(request):
    return HttpResponseRedirect('/dashboard/')


class Tnc(generic.TemplateView):
    template_name = 'GeneralApp/tnc.html'


class AboutUs(generic.TemplateView):
    template_name = 'GeneralApp/about.html'
