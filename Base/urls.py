from django.urls import path
from .views import home , unauth_error
urlpatterns = [
    path('', home ,name='home_page'),
    path('/unauthorized', unauth_error ,name='unauth_page'),
    
    ]
