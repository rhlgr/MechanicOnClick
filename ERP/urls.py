from django.urls import path
from .views import ( add_service  , employee_service_updates , employee_service_list , update_progress , dashboard , genrate_estimate,
 estimates , delete_estimate , approve_page , activate_employee , deactivate_employee , change_role , show_pay_slips , add_pay_slip , attendance
 ,attendance_table , mark_attendance , assign_task , get_tasks , tasks_list , update_task_status , employee_tasks , center_product_list , add_product,
 edit_product , sell_product , add_services , add_extra_services , add_service_product , view_service
 )
from .customer_views import (add_vehical , edit_vehical , info_vehical , customer_services , approve_service, approve_estimate, 
 service_updates , vehical_services )
urlpatterns = [
    # Vehical Paths
    path('vehical/add/', add_vehical ,name='add_vehical_page'),
    path('vehical/edit/<str:pk>', edit_vehical ,name='edit_vehical_page'),
    path('vehical/', info_vehical ,name='info_vehical_page'),
    path('vehical/services/<str:pk>', vehical_services ,name='vehical_services_page'),
    # Service Paths
    path('service/add/', add_service ,name='add_service_page'),
    path('services/add/<str:pk>', add_services ,name='add_services'),
    path('services/extra/add/<str:pk>', add_extra_services ,name='add_extra_services'),
    path('service/product/<str:pk>', add_service_product ,name='add_service_product'),
    path('services/', customer_services ,name='customer_service_page'),
    path('services/view/update/<str:pk>', service_updates , name ='customer_service_updates_page'),
    path('services/approve/<str:pk>', approve_service , name='approve_service'),
    path('services/update/<str:pk>', employee_service_updates , name ='employee_service_update_page'),
    path('services/list/', employee_service_list ,name='employee_service_list'),
    path('service/view/<str:pk>', view_service ,name='view_service_page'),
    path('services/update/progress/<str:pk>', update_progress , name ='progress_update_page'),
    path('dashboard/', dashboard , name ='dashboard'),
    #Estimate Paths
    path('estimate/gen/<str:pk>', genrate_estimate , name ='genrate_estimate'),
    path('estimates/', estimates , name ='estimates'),
    path('estimate/del/<str:pk>', delete_estimate , name ='delete_estimate'),
    path('estimate/approve/<str:pk>', approve_estimate , name ='approve_estimate'),
    # Admin Paths
    path('approve/', approve_page , name ='approve_page'),
    path('activate/<str:pk>', activate_employee , name ='activate_employee'),
    path('deactivate/<str:pk>', deactivate_employee , name ='deactivate_employee'),
    path('change/role/<str:pk>', change_role , name ='change_role'),
    # Pay Slip Paths
    path('payslip/view/<str:pk>', show_pay_slips , name ='pay_slips'),
    path('payslip/add/<str:pk>', add_pay_slip , name ='add_pay_slip'),
    #Attendance Paths
    path('attendance/', attendance , name ='attendance'),
    path('attendance/table', attendance_table , name ='attendance_table'),
    path('attendance/mark/<str:pk>/<str:date>', mark_attendance , name ='mark_attendance'),
    #Task Paths
    path('task/add', assign_task , name ='assign_task'),
    path('tasks/list', tasks_list , name ='tasks_list'),
    path('tasks/get', get_tasks , name ='get_tasks'),
    path('tasks/employee/get', employee_tasks , name ='employee_tasks'),
    path('task/status/update/<str:pk>',update_task_status,name = 'update_task_status'),
    # Product Paths
    path('products/', center_product_list , name ='center_product_list'),
    path('product/add', add_product , name ='add_product'),
    path('product/edit/<str:pk>', edit_product , name ='edit_product'),
    path('product/sell/<str:pk>/<str:sid>', sell_product , name ='sell_product'),
    ]
