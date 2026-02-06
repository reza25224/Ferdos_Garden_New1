from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time
import os
from .models import Workshop

#--------------------------------------------
def workshop_list(request):

    workshop = Workshop.objects.filter(is_active = True)
    context = {
        'workshop' : workshop,
        'media_url': settings.MEDIA_URL,
    }
    return render (request,'workshop_app/workshop_list.html',context)

#-------------------------------------------------------workshop_detaile
def workshop_detaile(request,id):
    workshop_detaile = Workshop.objects.get(id=id)
    context = {
        'workshop_detaile': workshop_detaile
    }
    return render (request , 'workshop_app/workshop_detaile.html', context)
