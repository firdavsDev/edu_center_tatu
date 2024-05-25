from django.contrib import admin

# Register your models here.
from .models import Profile, UserCourse, UserFinishedCourseLesson

admin.site.register(Profile)
admin.site.register(UserCourse)
admin.site.register(UserFinishedCourseLesson)
