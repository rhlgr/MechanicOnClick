from django.urls import path
from .views import add_vehical , edit_vehical
urlpatterns = [
    path('vehical/add/', add_vehical ,name='add_vehical_page'),
    path('vehical/edit/', edit_vehical ,name='edit_vehical_page'),
    
    ]
