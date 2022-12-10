from django.urls import path
from .views import home , about , services
urlpatterns = [
    path('', home ,name='home_page'),
    path('about/' , about, name='about_page'),
    path('service/' , services, name='service_page'),
]
