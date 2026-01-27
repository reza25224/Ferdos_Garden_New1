from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('history/',views.garden_history ,name='history'),
    path('section/',views.section_list , name='section'),
    path('section_detail/<int:id>/',views.section_detail ,name='section_detail'),
    path('visit_route/', views.visit_route , name = 'visit_route'),
    path('visiting_schedule',views.visiting_schedule , name = 'visiting_schedule'),
    path('contact_view',views.contact_view , name = 'contact_view'),

]


