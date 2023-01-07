from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.forms import ModelForm
#from django.contrib.auth.models import User
from .models import Customer , Employee

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"