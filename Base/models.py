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

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    subject = models.CharField(max_length=500, null=True , blank=True)
    message = models.CharField(max_length=500, null=True , blank=True) 

    def __str__(self) -> str:
        return self.name + '-' + self.subject
class Testimonial(models.Model):
    name = models.CharField(max_length=50, null=True , blank=True)
    profession = models.CharField(max_length=50, null=True , blank=True)
    content = models.CharField(max_length=500, null=True , blank=True)
    img = models.ImageField(upload_to='media/testimg', default= 'media/testimg/AviDP.jpeg')
    on_display = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class CarasouleElement(models.Model):
    img = models.ImageField(upload_to='media/carasouleimg')
    on_display = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = CarasouleElement.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except CarasouleElement.DoesNotExist:
                pass
        super(CarasouleElement, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title