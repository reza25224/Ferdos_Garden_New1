from django.db import models
from django.utils import timezone
from datetime import datetime
import os

#---------------------------------------------------save image name with time
def workshop_image_path(instance, filename):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = os.path.splitext(filename)[1]
    new_name = f"{now}{ext}"
    return f"images/workshop/{new_name}"


#---------------------------------------------------Workshop_Status
class WorkshopStatus(models.Model):
    id = models.AutoField(primary_key=True , verbose_name='کد وضعیت کارگاه')
    title = models.CharField(max_length=200 , verbose_name='عنوان کارگاه')

    def __str__(self):
        return self.title
    
    class Meta :
        verbose_name = 'وضعیت کارگاه'
        verbose_name_plural = 'وضعیت کارگاهها '
        db_table = 't_Workshop_Status'

#---------------------------------------------------Workshop
class Workshop (models.Model):
    id = models.AutoField(primary_key=True , verbose_name='کد کارگاه')
    title = models.CharField(max_length=200 , verbose_name='عنوان کارگاه')
    main_image = models.ImageField(upload_to=workshop_image_path , verbose_name='تصویر اصلی')
    date_event = models.DateTimeField(default=timezone.now , verbose_name='تاریخ و زمان برگزاری ')
    location = models.CharField(max_length=200 , verbose_name='مکان برگزاری')
    teacher = models.CharField(max_length=200 , verbose_name='مدرس')
    description = models.TextField(verbose_name='اطلاعات کارگاه ')
    register_way = models.TextField(verbose_name='نحوه ثبت نام')
    report_text = models.TextField(default='null' , null=True , verbose_name='متن گزارش کارگاه ')
    num_of_visit = models.IntegerField(default=0 , verbose_name='تعداد بازدید از گزارش')
    register_date = models.DateTimeField(default=timezone.now , verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=False , verbose_name='وضعیت فعال / غیر فعال')
    workshop_statue = models.ForeignKey(WorkshopStatus , on_delete=models.CASCADE , verbose_name='وضعیت کارگاه')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'کارگاه'
        verbose_name_plural = 'کارگاهها'
        db_table = ''

#------------------------------------------------------WorkshopGallery
class WorkshopGallery (models.Model):
    id = models.AutoField(primary_key=True ,verbose_name='کد تصویر')
    workshop = models.ForeignKey(Workshop , on_delete=models.CASCADE , verbose_name='کارگاه')
    name = models.CharField(max_length=100 , verbose_name='نام تصویر')
    imae = models.ImageField(upload_to=workshop , verbose_name='تصویر')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'تصویر کارگاه'
        verbose_name_plural ='تصاویر کارگاه '
        db_table = 't_WorkshopGallery'