from django import forms
from .models import  MessageToUs
#-----------------------------------------MessageForm
class MessageForm(forms.ModelForm):
    class Meta :
        model = MessageToUs
        fields = ['full_name','email','subject','mesage']