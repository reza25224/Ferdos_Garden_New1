from django.urls import path
from . import views

app_name = 'workshop'
urlpatterns = [
    path('workshop_list/',views.workshop_list,name='workshop_list'),
    path('workshop_detaile/<int:id>/',views.workshop_detaile , name='workshop_detaile'),

]