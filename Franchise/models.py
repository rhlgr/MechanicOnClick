from django.db import models

# Create your models here.

class Center(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class JobRole(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title