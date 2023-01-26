from django.db import models
from ERP.models import ProvidedService
from account.models import Employee
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    phone = models.CharField(max_length=50, null=True , blank=True)
    #date = models.DateField(null=True , blank=True)
    issue = models.CharField(max_length=200, null=True , blank=True)
    vehical = models.CharField(max_length=50, null=True , blank=True)

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

