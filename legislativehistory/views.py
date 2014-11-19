from django.shortcuts import render
from django.http import HttpResponse
from legislativehistory.models import *

def index(request):
    legislation = Legislation.objects.get()
    return render(request, 'index.html', {'legislation': legislation})

