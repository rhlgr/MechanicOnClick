from django.db import models
from django.contrib.auth.models import User
from Franchise.models import Center , JobRole
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.first_name

class Employee(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    center = models.ForeignKey(Center , on_delete= models.SET_NULL , blank=True , null= True)
    store = models.CharField(max_length=100)
    job_role = models.ForeignKey( JobRole, on_delete= models.SET_NULL, blank=True , null= True)

    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name 
