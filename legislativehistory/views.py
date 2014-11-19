from django.shortcuts import render
from django.http import HttpResponse
from legislativehistory.models import *

def index(request):
    return render(request, 'index.html')

def bill_detail(request, state, session):
    return render(request, 'bill_detail.html', {'state': state, 'session': session})

def legislation(request):
    legislation = Legislation.objects.all()
    return render(request, 'legislation.html', {'legislation': legislation})

