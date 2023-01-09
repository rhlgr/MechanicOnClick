from django.urls import path
from .views import add_vehical
urlpatterns = [
    path('vehicel/add/', add_vehical ,name='add_vehical_page'),
    #path('/unauthorized', unauth_error ,name='unauth_page'),
    
    ]
