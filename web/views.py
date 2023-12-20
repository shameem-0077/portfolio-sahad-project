from django.shortcuts import render
from .models import Event, Gallery


def index(request):
    events = Event.objects.all()
    gallery = Gallery.objects.all()
    context = {
        "title": "Home",
        "events": events,
        "gallery": gallery,
    }
    return render(request, "index.html", context=context)
