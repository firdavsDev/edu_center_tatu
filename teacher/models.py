from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='teacher/profile_pics')
    job_title = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
