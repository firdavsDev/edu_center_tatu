from django.db import models
from django.contrib.auth.models import User
from course.models import Coures, CourseLesson


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Coures, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'

    class Meta:
        verbose_name = 'User Course'
        verbose_name_plural = 'User Courses'


class UserFinishedCourseLesson(models.Model):
    enrolled_course = models.ForeignKey(
        UserCourse, on_delete=models.CASCADE, related_name='enrolled_course')
    lessons = models.ManyToManyField(
        CourseLesson, related_name='finished_lessons')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'

    class Meta:
        verbose_name = 'User Finished Lesson'
        verbose_name_plural = 'User Finished Lessons'
