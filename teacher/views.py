from django.shortcuts import render

# Create your views here.
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/list.html', {'teachers': teachers})
