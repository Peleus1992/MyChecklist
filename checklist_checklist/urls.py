from django.conf.urls import url

from . import views

urlpatterns = [
    url('checklist', views.checklist, name='checklist'),
]