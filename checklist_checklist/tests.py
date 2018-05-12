# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Checklist


class ChecklistTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # response = self.client.post(reverse('signup'),
        #                {'username': 'derek', 'email': 'derek@mail.com', 'password': 'qweqweqwe'})
        # self.assertEqual(302, response.status_code)

    def test_add_checklist(self):
        response = self.client.post(reverse('add_checklist'),
                                    {'title': 'one piece'})
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Checklist.objects.filter(title='one piece').count())
