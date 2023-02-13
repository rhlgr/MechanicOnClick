from django.forms import ModelForm , DateInput , Form
from .models import Service ,Update , Vehical ,PaySlip
from django import forms

# Widgets 
class DatePickerInput(DateInput):
    input_type = 'date'
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields ='__all__'
class UpdateForm(ModelForm):
    class Meta:
        model =Update
        fields = ['update_image','update_title' , 'update_description']
        #fields = '__all__'
class UpdateProgressForm(Form):
    #progress = forms.CharField(max_length=20 , choices=Service.Progress.choices , default= Service.Progress.WAITING)
    progress = forms.ChoiceField(choices= Service.Progress.choices )

class PaySlipForm(ModelForm):
    class Meta : 
        model = PaySlip
        fields = ['amount' , 'date' , 'slip' , 'txnid' ]
        #fields = '__all__'
        widgets = {
            'date' : DatePickerInput()
        }