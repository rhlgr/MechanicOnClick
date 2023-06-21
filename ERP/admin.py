from django.contrib import admin
from .models import Service , Vehical , Update , CenterServices , Estimate , PaySlip , Attendance , Task , CenterProduct , ProductSale

# Register your models here.

#admin.site.register(ProvidedService)
admin.site.register(Service)
admin.site.register(Update)
admin.site.register(Vehical)
admin.site.register(CenterServices)
admin.site.register(Estimate)
admin.site.register(PaySlip)
admin.site.register(Attendance)
admin.site.register(Task)
admin.site.register(CenterProduct)
admin.site.register(ProductSale)