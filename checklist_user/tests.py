# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.shortcuts import reverse


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        response = self.client.post(reverse('signup'),
                               {'username': 'derek', 'email': 'derek@mail.com', 'password': 'qweqweqwe'})
        self.assertEqual(302, response.status_code)

    def test_duplicate_signup_user(self):
        response = self.client.post(reverse('signup'),
                                    {'username': 'derek', 'email': 'derek@mail.com', 'password': 'qweqweqwe'})
        self.assertEqual(400, response.status_code)

    def test_login_user(self):
        response = self.client.post(reverse('login'), {'username': 'derek', 'password': 'wrongpassword'})
        self.assertEqual(400, response.status_code)
        response = self.client.post(reverse('login'), {'username': 'derek', 'password': 'qweqweqwe'})
        self.assertEqual(302, response.status_code)

    def test_logout_user(self):
        response = self.client.post(reverse('login'), {'username': 'derek', 'password': 'qweqweqwe'})
        self.assertEqual(302, response.status_code)
        response = self.client.post(reverse('logout'))
        self.assertEqual(302, response.status_code)