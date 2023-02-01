from django.contrib import admin
from .models import Center , JobRole , Location
# Register your models here.

admin.site.register(JobRole)
admin.site.register(Center)
admin.site.register(Location)
