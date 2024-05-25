from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='detail'),
    path('<int:course_id>/enroll/', views.course_enroll, name='enroll'),
    path('my-courses/', views.course_my_courses, name='my_courses'),
    path('my-courses/<int:course_id>/',
         views.course_my_course_detail, name='my_course_detail'),
    path('<int:course_id>/lesson/<int:lesson_id>/finished/',
         views.finsihed_lesson, name='finished_lesson'),
    path('<int:course_id>/lesson/<int:lesson_id>/',
         views.lesson_detail, name='lesson_detail')
]
