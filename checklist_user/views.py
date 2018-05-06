# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'GET':
        return render(request, 'checklist_user/signup_page.html')

    # POST request
    status_code = 200
    error_message = None
    if not all(arg in request.POST for arg in ['username', 'email', 'password']):
        status_code = 400
        error_message = 'Error: Username, email or password is not provided.'
    else:
        username = request.POST['username']
        if User.objects.filter(username=username).count():
            status_code = 400
            error_message = 'Error: User already exist.'
        else:
            status_code = 302
            email = request.POST['email']
            password = request.POST['password']
            User.objects.create_user(username, email, password)

    response = None
    if status_code == 302:
        response = redirect('checklist_user/login_page.html')
    else:
        response = render(request, 'checklist_user/signup_page.html', {'message': error_message})
    response.status_code = status_code
    return response


def login_view(request):
    if request.method == 'GET':
        return render(request, 'checklist_user/login_page.html')

    # POST request
    status_code = 200
    error_message = None
    if not all(arg in request.POST for arg in ['username', 'password']):
        status_code = 400
        error_message = 'Error: Username or password is not provided.'
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            status_code = 302
            login(request, user)
        else:
            status_code = 400
            error_message = 'Error: User not found.'

    response = None
    if status_code == 302:
        response = redirect(reverse('checklist:checklist'))
    else:
        response = render(request, 'checklist_user/login_page.html', {'message': error_message})
    response.status_code = status_code
    return response


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))