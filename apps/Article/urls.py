from django.urls import path
from . import views

app_name = 'Article'
urlpatterns = [
    path('',views.Article_view, name='Article_view'),
    path('add/',views.Article_create, name='Article_create'),
    path('article_detaile/<int:id>/',views.article_detaile , name='article_detaile'),
]