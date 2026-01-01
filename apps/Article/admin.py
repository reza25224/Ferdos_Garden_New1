from django.contrib import admin
from .models import *

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('id','name','family','education','job_title','email','slug','phone_number','is_active')


@admin.register(ArticleGroup)
class ArticleGroup(admin.ModelAdmin):
    list_display = ('id','title')

@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('id','article_group','title','main_image','authors_display','slug',
                    'description','abstract','keywords','pdf_name','register_date',
                    'publication_date','update_date','number_of_visit','is_active')
    
    def authors_display(self, obj):
        # فرض کنید فیلد ManyToMany شما با نام 'author' است
        return ", ".join([str(a) for a in obj.author.all()])
    authors_display.short_description = 'نویسندگان'
    
@admin.register(ArticleGallery)
class ArticleGallery(admin.ModelAdmin):
    list_display = ('id','article','name')