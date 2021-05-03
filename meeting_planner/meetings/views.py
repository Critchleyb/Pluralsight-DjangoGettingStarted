from django.shortcuts import render, get_object_or_404

from meetings.models import Meeting

def detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'meetings/detail.html', {"meeting": meeting})
