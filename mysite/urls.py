from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('contact/', include('contact.urls', namespace='contact')),
]
