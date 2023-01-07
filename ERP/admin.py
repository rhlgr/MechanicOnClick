from django.contrib import admin
from .models import ProvidedService , Service , Vehical , Update

# Register your models here.

admin.site.register(ProvidedService)
admin.site.register(Service)
admin.site.register(Update)
admin.site.register(Vehical)