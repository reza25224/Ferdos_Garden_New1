from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان مقاله')
    description =models.TextField(verbose_name='متن مقاله')
    is_active = models.BooleanField(default=False , verbose_name='وضعیت فعال/غیر فعال ')
    main_image = models.ImageField(upload_to='images/blog',verbose_name='تصویر اصلی ')
    register_date = models.DateTimeField(default=timezone.now , verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'وبلاک'
        verbose_name_plural = 'وبلاگ ها'
        db_table = 't_blog'