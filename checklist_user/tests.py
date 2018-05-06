# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.http import HttpResponse


class UserTestCase(TestCase):
    def setUp(self):
        pass

    def test_signup_user(self):
        client = Client()
        response = client.post('/user/signup/', {'username': 'derek', 'email': 'derek@mail.com', 'password': 'qweqweqwe'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("Success.", response.content)

    def test_duplicate_signup_user(self):
        self.test_signup_user()
        client = Client()
        response = client.post('/user/signup/', {'username': 'derek', 'email': 'derek@mail.com', 'password': 'qweqweqwe'})
        self.assertEqual(200, response.status_code)
        self.assertEqual("Error: User already exist.", response.content)