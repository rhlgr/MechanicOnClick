from django.db import models
from ERP.models import ProvidedService
from account.models import Employee
# Create your models here.
class Brand(models.Model):
    logo = models.ImageField(upload_to='/brands/logos')
    name = models.TextField(max_length=50)
    has_two_wheeler = models.BooleanField(default=True)
    has_four_wheeler = models.BooleanField(default=True)
class VechicalModel(models.Model):
    class FuleType(models.TextChoices):
        PETROL = 'PETROL' , 'PETROL'
        DIESEL = 'DIESEL' , 'DIESEL'
        CNG = 'CNG' , 'CNG'
    fule_type = models.TextField(max_length=50 , choices=FuleType.choices)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    name = models.TextField(max_length=50)

class Booking(models.Model):

    phone = models.CharField(max_length=50, null=True , blank=True)
    issue = models.CharField(max_length=200, null=True , blank=True)
    
    def __str__(self) -> str:
        return self.name 

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    subject = models.CharField(max_length=500, null=True , blank=True)
    message = models.CharField(max_length=500, null=True , blank=True) 
    
    def __str__(self) -> str:
        return str(self.name) + '-' + str(self.subject)
class Testimonial(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    profession = models.CharField(max_length=50, null=True , blank=True)
    content = models.CharField(max_length=500, null=True , blank=True)
    img = models.ImageField(upload_to='media/testimg', default= 'media/testimg/AviDP.jpeg')
    on_display = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

