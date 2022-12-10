from django.db import models
from ERP.models import ProvidedService
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    ProvidedServices = models.ForeignKey(ProvidedService,null=True , blank=True , on_delete=models.SET_NULL)
    date = models.DateField(null=True , blank=True)
    content = models.CharField(max_length=200, null=True , blank=True)