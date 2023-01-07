from django.urls import path 
from .views import customer_register
urlpatterns = [
    path('register', customer_register),
    
]