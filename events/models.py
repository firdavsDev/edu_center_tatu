from django.db import models
from teacher.models import Teacher


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='event/images')
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    is_published = models.BooleanField(default=False)
    speakers = models.ManyToManyField(
        Teacher, related_name='events', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.location}"

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
