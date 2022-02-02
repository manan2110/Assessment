from django.shortcuts import render
from api.views import find_age

# Create your views here.


def index(request):
    return render(request, "home.html")
