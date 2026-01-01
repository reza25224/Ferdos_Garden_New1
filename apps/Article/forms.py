from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta :
        model = Article
        fields = ['title','description', 'main_image','is_active','register_date']