from django.urls import path
from .views import home , unauth_error , service ,contact
urlpatterns = [
    path('', home ,name='home_page'),
    path('unauthorized/', unauth_error ,name='unauth_page'),
    path('service/', service ,name='service_page'),
    path('contact/', contact ,name='contact_page'),
    
    ]
