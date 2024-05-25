from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models

# Create your views here.
from .models import Coures, CourseLesson
from accounts.models import UserCourse, UserFinishedCourseLesson


def course_list(request):
    courses = Coures.objects.filter(is_published=True)
    return render(request, 'course/list.html', {'courses': courses})


def course_detail(request, course_id):
    course = Coures.objects.get(id=course_id)
    lessons = CourseLesson.objects.filter(course=course)
    return render(request, 'course/detail.html', {'course': course, 'lessons': lessons})


@login_required
def course_enroll(request, course_id):
    course = Coures.objects.get(id=course_id)
    user = User.objects.get(id=request.user.id)
    UserCourse.objects.get_or_create(user=user, course=course)
    messages.success(request, 'You have successfully enrolled in this course')
    return redirect('course:my_courses')


@login_required
def course_my_courses(request):
    user = User.objects.get(id=request.user.id)
    courses = UserCourse.objects.filter(user=user)
    return render(request, 'course/my_courses.html', {'courses': courses})


@login_required
def course_my_course_detail(request, course_id):
    my_course = Coures.objects.get(id=course_id)
    lessons = CourseLesson.objects.filter(course=my_course)
    # add lesson_is_finished to each lesson via a for loop
    for lesson in lessons:
        lesson.lesson_is_finished = UserFinishedCourseLesson.objects.filter(
            enrolled_course__user=request.user, enrolled_course__course=my_course, lessons=lesson).exists()

    return render(request, 'course/my_course_detail.html', {'lessons': lessons, 'my_course': my_course})


@login_required
def lesson_detail(request, course_id, lesson_id):
    course = Coures.objects.get(id=course_id)
    lesson = CourseLesson.objects.get(id=lesson_id)
    return render(request, 'course/lesson_detail.html', {'lesson': lesson, 'course': course})


@login_required
def finsihed_lesson(request, course_id, lesson_id):
    course = Coures.objects.get(id=course_id)
    lesson = CourseLesson.objects.get(id=lesson_id, course=course)
    user_course = UserCourse.objects.get(user=request.user, course=course)
    user_finished_lesson, _ = UserFinishedCourseLesson.objects.get_or_create(
        enrolled_course=user_course)
    user_finished_lesson.lessons.add(lesson)
    user_finished_lesson.save()
    messages.success(request, 'You have successfully finished this lesson')
    return redirect('course:my_course_detail', course_id=course_id)
