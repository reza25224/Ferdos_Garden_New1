from django.db import models
from django.utils import timezone
from datetime import datetime
import os

#---------------------------------------------------save image name with time
def article_image_path(instance, filename):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = os.path.splitext(filename)[1]
    new_name = f"{now}{ext}"
    return f"images/blog/{new_name}"

#---------------------------------------------------Author
class Author(models.Model):
    id = models.AutoField(primary_key=True ,verbose_name='کد نویسنده')
    name = models.CharField(max_length=100 , verbose_name='نام')
    family = models.CharField(max_length=100 , verbose_name='نام خانوادگی')
    education = models.CharField(max_length=100 , verbose_name='تحصیلات')
    job_title = models.CharField(max_length=100 , verbose_name='شغل')
    email = models.EmailField(unique=True , verbose_name='ایمیل')
    slug = models.SlugField(unique=True ,verbose_name='slug')
    phone_number = models.CharField(max_length=15 ,blank=True ,  verbose_name='شماره تلفن')
    is_active = models.BooleanField(default=False , verbose_name='وضعیت فعال/غیر فعال')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'
        db_table = 't_Author'

#---------------------------------------------------ArticleGroup
class ArticleGroup(models.Model):
    id = models.AutoField(primary_key=True , verbose_name='کد گروه')
    title = models.CharField(max_length=100 , verbose_name='عنوان گروه')

    def __str__(self):
        return self.title
    
    class  Meta:
        verbose_name = ' گروه مقاله'
        verbose_name_plural = 'گروه مقالات'
        db_table = 't_ArticleGroup'

#---------------------------------------------------Article
class Article(models.Model):
    id = models.AutoField(primary_key=True ,verbose_name='کد مقاله')
    article_group = models.ForeignKey(ArticleGroup , on_delete=models.CASCADE , verbose_name='گروه مقاله')
    title = models.CharField(max_length=200 , verbose_name='عنوان مقاله')
    main_image = models.ImageField(upload_to=article_image_path,verbose_name='تصویر اصلی ')
    author= models.ManyToManyField(Author,related_name='articles',verbose_name='نویسنده')
    slug = models.SlugField(unique=True,max_length=200 ,verbose_name='slug')
    description =models.TextField(verbose_name='متن کوتاه')
    abstract = models.TextField(verbose_name='چکیده مقاله')
    keywords = models.CharField (max_length=100 , verbose_name='کلمات کلیدی')
    pdf_name = models.CharField (max_length=100 , verbose_name='نام فایل اصلی مقاله')
    register_date = models.DateTimeField(default=timezone.now , verbose_name='تاریخ ثبت')
    publication_date = models.DateTimeField(null=True, blank=True ,verbose_name='تاریخ انتشار')
    update_date = models.DateTimeField(auto_now=True ,verbose_name='تاریخ به روز رسانی')
    number_of_visit = models.IntegerField(default=0,verbose_name='تعداد بازدید')
    is_active = models.BooleanField(default=False , verbose_name='وضعیت فعال/غیر فعال ')    
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        db_table = 't_Article'

#-------------------------------------------------ArticleGallery 
class ArticleGallery(models.Model):
    id = models.AutoField(primary_key=True ,verbose_name='کد تصویر')
    article = models.ForeignKey(Article , on_delete=models.CASCADE , verbose_name='مقاله')
    name = models.CharField(max_length=100 , verbose_name='نام نصویر')

    def __str__(self):
        return self.name
    
    class Meta :
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'
        db_table = 't_ArticleGallery'
    