from django.shortcuts import render
from .models import Event


def index(request):
    events = Event.objects.all()
    context = {
        "title": "Home",
        "events": events,
    }
    return render(request, "index.html", context=context)
