
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Add this import
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # index page
    path('', home, name='home'),
    path('contact/', include('contact.urls')),
    path('auth/', include('accounts.urls')),
    path('teacher/', include('teacher.urls')),
    path('events/', include('events.urls')),
    path('courses/', include('course.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
