from django.urls import path
from .views import add_vehical , edit_vehical , info_vehical , add_service , customer_services , approve_service , service_updates , employee_service_updates , employee_service_list , update_progress
urlpatterns = [
    path('vehical/add/', add_vehical ,name='add_vehical_page'),
    path('vehical/edit/<str:pk>', edit_vehical ,name='edit_vehical_page'),
    path('vehical/', info_vehical ,name='info_vehical_page'),
    path('service/add/', add_service ,name='add_service_page'),
    path('services', customer_services ,name='customer_service_page'),
    path('services/view/update/<str:pk>', service_updates , name ='customer_service_updates_page'),
    path('services/approve/<str:pk>', approve_service),
    path('services/update/<str:pk>', employee_service_updates , name ='employee_service_update_page'),
    path('services/list', employee_service_list ,name='employee_service_list'),
    path('services/update/progress/<str:pk>', update_progress , name ='progress_update_page'),
    
    
    ]
