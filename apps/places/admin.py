from django.contrib import admin
from .models import *

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title','image','visiting_day','visiting_hour','register_date')

@admin.register(VisitorsType)
class VisitorsType(admin.ModelAdmin):
    list_display = ('type_name',)

@admin.register(TicketPrice)
class TicketPrice(admin.ModelAdmin):
    list_display = ('place','visitor_type','price')


@admin.register(MessageToUs)
class MessageToUs(admin.ModelAdmin):
    list_display = ('full_name','email','subject','mesage','is_seen','register_date')
