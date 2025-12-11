from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta :
        model = Blog
        fields = ['title','description', 'main_image','is_active','register_date']