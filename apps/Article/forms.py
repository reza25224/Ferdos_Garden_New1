from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta :
        model = Article
        fields = ['article_group','title','main_image','author','slug','description', 'slug','keywords','pdf_name','register_date','publication_date','number_of_visit','is_active']