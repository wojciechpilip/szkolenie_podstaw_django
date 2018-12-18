from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello_world(request):
    return HttpResponse("HelloWorld")


def hello_name(request, name, last_name=""):
    out = f"Hello {name}"
    if last_name:
        out += f" {last_name}"
    return HttpResponse(out)



