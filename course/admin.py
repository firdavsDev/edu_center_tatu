from django.contrib import admin

# Register your models here.
from .models import Coures, CourseLesson


class CourseLessonInline(admin.TabularInline):
    model = CourseLesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseLessonInline]
    list_display = ['name', 'teacher', 'price', 'duration', 'created_at']
    search_fields = ['name', 'teacher']
    list_filter = ['teacher', 'created_at']
    list_editable = ['price']


admin.site.register(Coures, CourseAdmin)
admin.site.register(CourseLesson)
