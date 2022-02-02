from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("find_age", views.find_age),
]
