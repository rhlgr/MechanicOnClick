from django.urls import path
from .views import home , about , services , booking , contact
urlpatterns = [
    path('', home ,name='home_page'),
    path('about/' , about, name='about_page'),
    path('service/' , services, name='service_page'),
    path('booking/' , booking, name='booking_page'),
    path('contact/' , contact, name='contact_page'),
    ]
