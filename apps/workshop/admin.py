from django.contrib import admin
from .models import *

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title','main_image','date_event','num_of_visit','is_active','workshop_statue')

@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display = ('title',)

