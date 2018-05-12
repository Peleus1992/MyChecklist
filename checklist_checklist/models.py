# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Checklist(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChecklistItem(models.Model):
    checklist = models.ForeignKey(Checklist, models.CASCADE)
    text = models.CharField(max_length=1000)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


