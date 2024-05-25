from django.db import models

from teacher.models import Teacher


class Coures(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='course/images')
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    price = models.IntegerField()
    duration = models.IntegerField(help_text='Duration in days')
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.teacher.name}"


class CourseLesson(models.Model):
    course = models.ForeignKey(Coures, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    youtube_url = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.course.name}"
