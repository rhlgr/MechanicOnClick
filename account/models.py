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
    base_role = Role.CUSTOMER
    phone = models.CharField(max_length=13,unique=True , null=True , blank=True)
    role = models.CharField(max_length=50 , choices=Role.choices)

    def save(self, *args , **kwargs):
        if not self.pk :
            self.role = self.base_role
        return super().save(*args,**kwargs)


class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , null= True , blank= True)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.first_name

class Employee(models.Model):
    emp_img = models.ImageField(upload_to='media/empimg', default= 'media/empimg/AviDP.jpeg')
    user = models.OneToOneField(User , on_delete=models.CASCADE , null= True , blank= True)
    center = models.ForeignKey(Center , on_delete= models.SET_NULL , blank=True , null= True)
    store = models.CharField(max_length=100)
    job_role = models.ForeignKey( JobRole, on_delete= models.SET_NULL, blank=True , null= True)
    on_emp_display = models.BooleanField(default=False)
    on_tech_display = models.BooleanField(default=False)
    facbook_link = models.CharField(max_length=100, blank=True , null=True)
    twitter_link = models.CharField(max_length=100, blank=True , null=True)
    insta_link = models.CharField(max_length=100, blank=True , null=True)
    is_active = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.user.first_name + " "+ self.UserModel.last_name
