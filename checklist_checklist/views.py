# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def checklist(request):
    return render(request, 'checklist_checklist/checklist_page.html')
