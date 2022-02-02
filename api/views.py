from django.shortcuts import render
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET"])
def find_age(request):
    day = int(request.GET.get("day"))
    month = int(request.GET.get("month"))
    year = int(request.GET.get("year"))
    birthdate = date(year, month, day)
    today = date.today()
    check = (today.month, today.day) < (
        birthdate.month,
        birthdate.day,
    )  # leaping is covered in this condition
    year_difference = today.year - birthdate.year
    age = year_difference - check
    return Response(data={"age": age}, status=status.HTTP_200_OK)
