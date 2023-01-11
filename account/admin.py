from django.contrib import admin
from .models import Employee , Customer , User , EmployeeAdmin
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(EmployeeAdmin)


