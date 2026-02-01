from django.shortcuts import render , redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time
import os
from .models import Workshop

#--------------------------------------------
def workshop_list(request):
    workshop = Workshop.objects.all()
    context = {
        'workshop' : workshop
    }
    return render (request,'workshop_app/workshop_list.html', context)
