from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from Franchise.models import Center , JobRole
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN" , "Admin"
        CUSTOMER = 'CUSTOMER' , "Customer"
        EMPLOYEE = 'EMPLOYEE' , 'Employee'
        NA = 'NA' , 'NA'
    #base_role = Role.CUSTOMER
    phone = models.CharField(max_length=13,unique=True , null=True , blank=True)
    role = models.CharField(max_length=50 , choices=Role.choices ,default= Role.CUSTOMER)
    is_active = models.BooleanField(default=False)

    


class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null= True , blank= True)
    location = models.CharField(max_length=200)
    #is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.first_name

class Employee(models.Model):
    #emp_img = models.ImageField(upload_to='media/empimg', default= 'media/empimg/AviDP.jpeg')
    user = models.OneToOneField(User , on_delete=models.CASCADE , null= True , blank= True)
    center = models.ForeignKey(Center , on_delete= models.SET_NULL , blank=True , null= True)

    #is_active = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name
class EmployeeAdmin(models.Model):
    emp_img = models.ImageField(upload_to='media/empimg', default= 'media/empimg/AviDP.jpeg')
    user = models.OneToOneField(User , on_delete=models.CASCADE , null= True , blank= True)
    center = models.ForeignKey(Center , on_delete= models.SET_NULL , blank=True , null= True)

    #is_active = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name