from django.db import models
from django.utils import timezone

#--------------------------------------------------------------------------------------
class Place(models.Model):
    title = models.CharField(max_length=100 , verbose_name='نام مکان')
    description = models.TextField(verbose_name='توضیحات' , default='description')
    image = models.ImageField(upload_to='images/places/', verbose_name='تصویر')
    visiting_day = models.CharField(max_length=100,verbose_name='روزهای بازدید')
    visiting_hour = models.CharField(max_length=100 , verbose_name='ساعت بازدید')
    ruls = models.TextField(verbose_name='قوانین')
    register_date = models.DateTimeField(default=timezone.now,verbose_name='تاریخ و زمان ثبت')

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مکان'
        verbose_name_plural = 'مکان ها'
        db_table = 't_Places'

#--------------------------------------------------------------------------------------
class VisitorsType(models.Model):
    type_name = models.CharField(max_length=100 , verbose_name='نوع بازدید کننده')

    def __str__(self):
        return self.type_name
    
    class Meta:
        verbose_name = ' نوع بازدید کننده'
        verbose_name_plural ='بازدید کنندگان'
        db_table = 't_visitors_type'

#--------------------------------------------------------------------------------------
class TicketPrice(models.Model):
    place = models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name='مکان')
    visitor_type = models.ForeignKey(VisitorsType,on_delete=models.CASCADE,verbose_name='گروه بازدید')
    price = models.IntegerField(default=0 , verbose_name='بهای بلیط')

    def __str__(self):
        return f'{self.place}\t {self.visitor_type}\t {self.price}'
    
    class Meta:
        verbose_name = 'قیمت'
        verbose_name_plural ='قیمت ها'
        db_table = 't_ticket_price'

        
