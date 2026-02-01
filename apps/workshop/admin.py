from django.contrib import admin
from .models import *

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('main_image','title','date_event')

@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display = ('title',)

