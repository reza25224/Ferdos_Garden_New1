from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Place

#---------------------------------------------------------
def garden_history(request):
    return render(request,'place_app/history.html')

def garden_section(request):
    return render (request,'place_app/section.html')

#----------------------------------------------------------
# class SectionList(ListView):
#     model=Place
#     paginate_by = 5

def section_list(request):
    sections = Place.objects.all()
    context = {
        'section':sections
    }
    return render (request , 'place_app/section.html', context)

def section_detail(request,id):
    section_detail = Place.objects.get(id=id)
    context = {
        'section_detail':section_detail
    }
    return render(request,'place_app/section_detail.html',context)