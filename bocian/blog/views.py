from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

from blog.models import Wpis

# Create your views here.

def index(reqest):
    wpisy = Wpis.objects.all()
    out = ""
    for w in wpisy:
        out += f"{w.tytul}<br>"

    return HttpResponse(out)

def index_temp(request):
    ostatni_wpis = Wpis.objects.last()
    t = loader.get_template('blog/index.html')
    liczby = [x for x in range(10)]
    context = {
        'chleb':'1.90',
        'woda':2.5,
        'wpis': ostatni_wpis,
        'liczby': liczby
    }
#    wynik = t.render(context)
#    return HttpResponse(wynik) - to samo co ponizej
    return render(
        request=request,
        template_name='blog/index.html',
        context=context
        )