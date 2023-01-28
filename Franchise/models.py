from django.db import models

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
class Center(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location , null=True , blank= True , on_delete= models.SET_NULL)
    #location = models.CharField(max_length=100, null=True , blank= True)
    def __str__(self) -> str:
        return self.name

class JobRole(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
