from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from legislativehistory.models import *

def index(request):
    return render(request, 'index.html')

def bill_detail(request, state_slug, session, bill_number_slug):
    # TODO change all refs to "session_year" to "session"
    l = get_object_or_404(Legislation, state_slug=state_slug, session_year=session, bill_number_slug=bill_number_slug)
    return render(request, 'bill_detail.html', {'legislation': l})

def legislation(request):
    legislation = Legislation.objects.all()
    return render(request, 'legislation.html', {'legislation': legislation})

