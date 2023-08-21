from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryScreen, name="title"),
    path("search/", views.search, name="search"),
    path("randomEntry", views.randomEntry, name="random")
]
