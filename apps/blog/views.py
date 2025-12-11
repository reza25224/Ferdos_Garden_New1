from django.shortcuts import render
from .forms import BlogForm
from .models import Blog


def blog_view(request):
    return render (request , 'blog_app/blog.html')

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            blog = Blog()
            blog.title = data['title']
            blog.description = data['description']
            blog.is_active = data['is_active']
            blog.main_image = data['main_image']
            blog.register_date = data['register_date']
            blog.save()
            return render(request, 'blog_app/blog.html')
    else:
        form = BlogForm()

    context = {
        'form': form,
    }
    return render(request, 'blog_app/create.html', context)

