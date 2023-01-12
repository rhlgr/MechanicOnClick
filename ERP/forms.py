from django.forms import ModelForm , Form
from .models import Service
from django import forms
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields ='__all__'
class UpdateForm(Form):
    update_image = forms.ImageField(upload_to='media/updateimg' , blank= True , null= True)
    update_title = forms.CharField(max_length=50 , blank= True , null= True)
    update_description = forms.CharField(max_length = 200)