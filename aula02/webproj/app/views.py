from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import json

# Create your views here.

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)


def cv(request, num):
    name = "app/data/eurocv" + str(num) + ".json"
    f = open(name).read()
    tparams = {
        'cv': json.loads(f),
        'num': num,
    }
    return render(request, 'eurocv.html', tparams)
