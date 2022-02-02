from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("find_age", find_age, name="find_age"),
]
