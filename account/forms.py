from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.forms import ModelForm
#from django.contrib.auth.models import User
from .models import Customer , Employee ,User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'role' ,'first_name' , 'last_name','email'  ,'phone' , 'password1' , 'password2']
class RoleForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'role']
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['center']