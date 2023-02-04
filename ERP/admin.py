from django.contrib import admin
from .models import Service , Vehical , Update , CenterServices , Estimate

# Register your models here.

#admin.site.register(ProvidedService)
admin.site.register(Service)
admin.site.register(Update)
admin.site.register(Vehical)
admin.site.register(CenterServices)
admin.site.register(Estimate)