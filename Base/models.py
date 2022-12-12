from django.db import models
from ERP.models import ProvidedService
from account.models import Employee
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    ProvidedServices = models.ForeignKey(ProvidedService,null=True , blank=True , on_delete=models.SET_NULL)
    date = models.DateField(null=True , blank=True)
    content = models.CharField(max_length=200, null=True , blank=True)

    def __str__(self) -> str:
        return self.name 
class EmployeeDisplay(models.Model):
    title = models.CharField(max_length=50, null=True , blank=True)
    employees = models.ManyToManyField(Employee)
    
    is_active = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = EmployeeDisplay.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except EmployeeDisplay.DoesNotExist:
                pass
        super(EmployeeDisplay, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    subject = models.CharField(max_length=500, null=True , blank=True)
    message = models.CharField(max_length=500, null=True , blank=True) 

    def __str__(self) -> str:
        return self.name + '-' + self.subject