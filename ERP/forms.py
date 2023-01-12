from django.forms import ModelForm , Form
from .models import Service
from django import forms
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields ='__all__'
class UpdateForm(Form):
    update_image = forms.ImageField()
    update_title = forms.CharField(max_length=50 )
    update_description = forms.CharField(max_length = 200)
class UpdateProgressForm(Form):
    #progress = forms.CharField(max_length=20 , choices=Service.Progress.choices , default= Service.Progress.WAITING)
    progress = forms.ChoiceField(choices= Service.Progress.choices )