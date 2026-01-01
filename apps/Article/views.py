from django.shortcuts import render , redirect
from .forms import ArticleForm
from .models import Article
from django.core.files.storage import FileSystemStorage
import time
import os
from django.conf import settings



#--------------------------------------------------------------------------------------------------------
def Article_view(request):
    article = Article.objects.all()
    context = {
        'Articles' : article,
        'media_url': settings.MEDIA_URL,
    }

    
    return render (request , 'article_app/article.html',context)
    
#------------------------------------------------------------------------------------------
def Article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            image = request.FILES.get('main_image')

            # # ساختن نام جدید با زمان
            # timestamp = int(time.time())
            # ext = os.path.splitext(image.name)[1] # پسوند فایل
            # new_name = f'{timestamp}{ext}'

            # بررسی سایز
            if image.size > 100 * 1024:
                return render(request, 'blog_app/create.html', {
                    'form': form,
                    'message': 'سایز تصویر بیش از 100 کیلوبایت است'
                })

            # بررسی نوع فایل
            if image.content_type not in ['image/jpeg', 'image/png']:
                return render(request, 'blog_app/create.html', {
                    'form': form,
                    'message': 'نوع فایل نادرست است'
                })

            form.save()  # Django خودش فایل را ذخیره می‌کند
            return redirect('Article:Article_view')

    else:
        form = ArticleForm()

    return render(request, 'article_app/create.html', {'form': form})


