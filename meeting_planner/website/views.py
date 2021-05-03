from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html", {"meeting_count": Meeting.objects.count()})
    
def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

