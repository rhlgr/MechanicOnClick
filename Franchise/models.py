from django.db import models

# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    def __str__(self) -> str:
        return str(self.city) + '-' + str(self.pincode)
class Center(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location , null=True , blank= True , on_delete= models.SET_NULL)
    code = models.CharField(max_length=12 , unique=True , null=True , blank= True)
    #location = models.CharField(max_length=100, null=True , blank= True)
    def __str__(self) -> str:
        return self.name

class JobRole(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
