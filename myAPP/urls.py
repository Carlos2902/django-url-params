from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path("showform/", views.showform, name="form"),
    path("getform/", views.getform, name="GETFORM")
]