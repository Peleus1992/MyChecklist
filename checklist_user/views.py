# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signup_view(request):
    username = request.POST['username']
    if User.objects.filter(username=username).count():
        return HttpResponse("Error: User already exist.")

    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    if user is not None:
        return HttpResponse("Success.")
    return HttpResponse("Error: Unknown.")


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return HttpResponse("Error: User not found.")


def logout_view(request):
    login(request)
    return HttpResponse("Success.")