from django.db import models
from account.models import Customer
from Franchise.models import Center
# Create your models here.

class Vehical(models.Model):
    customer = models.OneToOneField(Customer , on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.number
class ProvidedService(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    renew_time = models.DurationField()
    price = models.IntegerField(default=500)

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    vehical = models.ForeignKey(Vehical , on_delete=models.SET_NULL, blank=True , null= True)
    service_time = models.DurationField()
    service_date = models.DateTimeField()
    center = models.ForeignKey(Center , on_delete=models.SET_NULL, blank=True , null= True)
    progress_choices = [
        ('RO Open' , 'RO Open'),
        ('Step 2' , 'Step 2'),
        ('Step 3' , 'Step 3'),
    ]
    progress = models.CharField(max_length=20 , choices=progress_choices , default= 'Step 1')
    # Customer Already in vehical
    #customer = models.ForeignKey(Customer , on_delete=models.SET_NULL, blank=True , null= True)
    services = models.ManyToManyField(ProvidedService)

    def __str__(self) -> str:
        return self.vehical.number + " " + str(self.service_date)

