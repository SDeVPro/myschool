from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),#127.0.0.1:8000
    path('home/',include('home.urls')),#127.0.0.1:8000/home
    path('ckeditor',include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
