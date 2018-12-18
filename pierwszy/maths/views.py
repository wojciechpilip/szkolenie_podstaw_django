from django.shortcuts import render
from django.http import HttpResponse
from maths.models import Math

# Create your views here.

def operacje(request, operacja, liczba1, liczba2):
    if operacja == "add":
        liczba = liczba1 + liczba2
    elif operacja == "sub":
        liczba = liczba1 - liczba2
    elif operacja == "div":
        liczba = liczba1 / liczba2

    m = Math.objects.create(
        operation=operacja,
        arg1=liczba1,
        arg2=liczba2
    )

    return HttpResponse(f"Wynik {liczba}")
