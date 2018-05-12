from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.checklist, name='checklist'),
    path(r'<int:checklist_id>/', views.checklist_item, name='checklist_item'),
    path(r'add/', views.add_checklist, name='add_checklist'),
    path(r'<int:checklist_id>/remove/', views.remove_checklist, name='remove_checklist'),
    path(r'<int:checklist_id>/add/', views.add_checklist_item, name='add_checklist_item'),
    path(r'<int:checklist_id>/<int:checklist_item_id>/remove/',
        views.remove_checklist_item, name='remove_checklist_item'),
]
