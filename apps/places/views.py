from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Place,TicketPrice
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

#تاریخچه----------------------------------------------------------
def garden_history(request):
    return render(request,'place_app/history.html')

def garden_section(request):
    return render (request,'place_app/section.html')

#بخش های باغ----------------------------------------------------------
# class SectionList(ListView):
#     model=Place
#     paginate_by = 5

def section_list(request):
    sections = Place.objects.all()
    context = {
        'section':sections
    }
    return render (request , 'place_app/section.html', context)

#--------------------------------detail
def section_detail(request,id):
    section_detail = Place.objects.get(id=id)
    context = {
        'section_detail':section_detail
    }
    return render(request,'place_app/section_detail.html',context)

#مسیر بازدید----------------------------------------------------------
def visit_route(request):
    fs = FileSystemStorage()
    file_name = 'pdfs/ferdowsGardenPath.pdf'
    if fs.exists(file_name):
      with fs.open(file_name) as pdf :
            response=  HttpResponse(pdf, content_type = 'application/pdf')
            response ['Content-Disposition']='attachment; filename = ferdowsGardenPath.pdf'
            return response
    else: 
         return HttpResponseNotFound('file not found .....')

#برنامه بازدید----------------------------------------------------------
def visiting_schedule (request):
   place = Place.objects.all()
   price = TicketPrice.objects.all()
   context ={
       'place' :place,
       'price' :price
   }
   return render ( request ,'place_app/visiting_schedule.html',context)