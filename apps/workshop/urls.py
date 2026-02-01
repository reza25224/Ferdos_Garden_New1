from django.urls import path
from . import views

app_name = 'workshop'
urlpatterns = [
    path('workshop_list/',views.workshop_list,name='workshop_list'),
]