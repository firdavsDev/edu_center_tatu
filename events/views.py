from django.shortcuts import render

from .models import Event


def event_list(request):
    events = Event.objects.filter(is_published=True)
    return render(request, 'events/list.html', {'events': events})
