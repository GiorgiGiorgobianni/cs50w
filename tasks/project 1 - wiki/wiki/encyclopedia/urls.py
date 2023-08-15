from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entryScreen, name="title"),
    path("search/", views.searchEntries, name="search"),
    path("createEntry/", views.newEntry, name="newEntry"),
    path("randomEntry/", views.randomEntry, name="randomEntry"),
    path("edit/", views.editEntry, name="edit"),
    path("save/", views.saveEdit, name="save"),
]
