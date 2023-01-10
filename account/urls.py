from django.urls import path 
from .views import customer_register , customer_login
urlpatterns = [
    path('register/', customer_register , name="customer_register"),
    path('login/', customer_login , name="customer_login"),
    path('logout/', customer_login , name="logout"),
    
]