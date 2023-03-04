from django.urls import path 
from .views import customer_register , login , employee_register , customer_logout 
urlpatterns = [
    path('register/', customer_register , name="customer_register"),
    path('login/', login , name="login_page"),
    path('logout/', customer_logout , name="logout"),
    path('employee/register/', employee_register , name="employee_register"),
    #path('employee/admin/register/', admin_register , name="employee_admin_register"),
    
]