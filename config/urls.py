
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main.urls', namespace='main'),name='main'),
    path('places/',include('apps.places.urls',namespace='places'),name='places'),
    path('blog/',include('apps.blog.urls',namespace='blog'),name='blog')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
