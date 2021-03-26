from django.http import HttpResponse
from django.shortcuts import render

from app.models import Author, Book, Publisher


# Create your views here.
def all(request):
    tparams = {'books': Book.objects.all(), }
    return render(request, 'all.html', tparams)


def details(request, num):
    tparams = {'book': Book.objects.all()[num], 'num':num}
    return render(request, 'details.html', tparams)
