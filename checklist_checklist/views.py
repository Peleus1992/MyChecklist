# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Checklist, ChecklistItem


def checklist(request):
    checklist_list = Checklist.objects.all()
    return render(request, 'checklist_checklist/checklist_page.html', {'checklist_list': checklist_list})


def checklist_item(request, checklist_id):
    c = get_object_or_404(Checklist, pk=checklist_id)
    checklist_item_list = c.checklistitem_set.all()
    return render(request, 'checklist_checklist/checklist_item_page.html',
                  {'checklist': c, 'checklist_item_list': checklist_item_list})


def add_checklist(request):
    if 'title' not in request.POST:
        raise Http404('Error: Title should be provided.')

    title = request.POST['title']
    cl = Checklist(title=title)
    cl.save()
    return redirect(reverse('checklist'))


def remove_checklist(request, checklist_id):
    c = get_object_or_404(Checklist, pk=checklist_id)
    c.delete()
    return redirect(reverse('checklist'))


def add_checklist_item(request, checklist_id):
    if 'text' not in request.POST:
        raise Http404('Error: Text should be provided.')

    text = request.POST['text']
    c = get_object_or_404(Checklist, pk=checklist_id)
    c.checklistitem_set.create(text=text) # Not sure checklist_item_set or checklistitem_set?
    return redirect(reverse('checklist_item', kwargs={'checklist_id': checklist_id}))


def remove_checklist_item(request, checklist_id, checklist_item_id):
    i = get_object_or_404(ChecklistItem, pk=checklist_item_id)
    i.delete()
    return redirect(reverse('checklist_item', kwargs={'checklist_id': checklist_id}))