from django.shortcuts import render

from events.models import Event
from course.models import Coures
from teacher.models import Teacher


def home(request):
    """A view that displays a main page."""
    events = Event.objects.all().order_by('-created_at')[:3]
    courses = Coures.objects.all().order_by('-created_at')[:3]
    teachers = Teacher.objects.all().order_by('-created_at')[:3]

    context = {
        'events': events,
        'courses': courses,
        'teachers': teachers,
    }
    return render(request, 'index.html', context)
