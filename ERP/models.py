from django.db import models
from account.models import Customer
from Franchise.models import Center
# Create your models here.

class Vehical(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    number = models.CharField(max_length=20 , unique= True)
    type = models.CharField(max_length=20)
    def save(self,*args , **kwargs):
        self.number = self.number.upper()
        return super().save(*args , **kwargs)
    def __str__(self) -> str:
        return self.number
class ProvidedService(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400, default="Diam dolor diam ipsum sit amet diam et eos erat ipsum")
    duration = models.DurationField()
    renew_time = models.DurationField()
    price = models.IntegerField(default=500)
    on_display = models.BooleanField(default=False)
    icon = models.CharField(max_length=50 , default="fa fa-certificate fa-3x text-primary flex-shrink-0")

    def __str__(self) -> str:
        return self.name + " : " + str(self.price)

class Service(models.Model):
    
    vehical = models.ForeignKey(Vehical , on_delete=models.SET_NULL, blank=True , null= True)
    #service_time = models.DurationField()
    #service_date = models.DateTimeField()
    service_estimate = models.FloatField(default= 100)
    center = models.ForeignKey(Center , on_delete=models.SET_NULL, blank=True , null= True)
    progress_choices = [
        ('RO Open' , 'RO Open'),
        ('Step 2' , 'Step 2'),
        ('Step 3' , 'Step 3'),
    ]
    progress = models.CharField(max_length=20 , choices=progress_choices , default= 'Step 1')
    # Customer Already in vehical
    services = models.ManyToManyField(ProvidedService)
    additional_services = models.CharField(max_length=200, blank = True , null = True)
    #additional_services_cost = models.IntegerField(blank = True , null = True)
    is_approved = models.BooleanField(default=False)
    #customer = models.ForeignKey(Customer , on_delete=models.SET_NULL, blank=True , null= True)

    def __str__(self) -> str:
        return self.vehical.number


class Update(models.Model):
    update_image = models.ImageField(upload_to='media/updateimg' , blank= True , null= True)
    update_title = models.CharField(max_length=50 , blank= True , null= True)
    update_description = models.CharField(max_length=200 , blank= True , null= True)
    service = models.ForeignKey(Service , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.update_title
    