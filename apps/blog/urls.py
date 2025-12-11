from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.blog_view, name='blog_view'),
    path('add/',views.blog_create, name='blog_create'),
]