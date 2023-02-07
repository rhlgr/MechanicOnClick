from django.shortcuts import render , redirect
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm , UpdateProgressForm
from account.models import User , Customer , Employee
from .models import Vehical  ,Service , Update , CenterServices , Estimate
from django.contrib import messages
from .reports import make_report
import os
from account.forms import RoleForm
from MOC.settings import MEDIA_ROOT , BASE_DIR
# Customer Views :- Vehicals
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def add_vehical(request):
    context = {}
    if request.method == 'POST':
        try :
            user = request.user
            customer = Customer.objects.get(user = user)
            vehicalnumber = request.POST['vehicalnumber']
            vechicaltype = request.POST['vehicaltype']
            new_vehcial =  Vehical.objects.create(customer = customer , number = vehicalnumber , type = vechicaltype)
            new_vehcial.save()
        except Exception as e:
            print(e)
            messages.error(request, 'Error in adding Vehical')
            return redirect('add_vehical_page')
    
    return render(request , 'ERP/vehical/add_vehical_page.html' , context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def edit_vehical(request , pk):
  
    vehical = Vehical.objects.get(id = pk)
    #print(vehicals)
    context = {'vehical' : vehical}
    if request.method == 'POST':
        try :
            user = request.user
            #print(user)
            customer = Customer.objects.get(user = user)
            vehical_id = pk
            vehicalnumber = request.POST['vehicalnumber']
            vehicaltype = request.POST['vehicaltype']
            #print('info 1 :',vehicaltype , vehicalnumber , vehical_id)
            vehical =  Vehical.objects.get(id = 1)
            if len(vehicalnumber) == 0:
                vehicalnumber = vehical.number
            if len(vehicaltype) == 0:
                vehicaltype = vehical.type
            #print('info 2 :',vehicaltype , vehicalnumber , vehical_id)
            vehical.number = vehicalnumber
            vehical.type = vehicaltype
            vehical.save()
            return redirect('info_vehical_page')
        except Exception as e :
            print(e)
            messages.error(request, 'Error in Editing Vehical. Please try again')
            return redirect('edit_vehical_page')
    return render(request , 'ERP/vehical/edit_vehical_page.html' , context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def info_vehical(request):
    user = request.user
    #print(user)
    customer = Customer.objects.get(user = user)
    vehicals = list(Vehical.objects.filter(customer = customer))
    #print(vehicals)
    context = {'vehicals' : vehicals}
    return render(request , 'ERP/vehical/info_vehical_page.html' , context)
#Customer :- Service Views
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def customer_services(request):
    vehicals = Vehical.objects.filter(customer = Customer.objects.get(user=request.user))
    context = {}
    app_services = Service.objects.filter(is_approved = True , vehical__in = vehicals)
    #app_services = Service.objects.filter(is_approved = True )
    not_app_services = Service.objects.filter(is_approved = False, vehical__in = vehicals)
    context['app_services'] = app_services
    context['not_app_services'] = not_app_services
    return render(request , 'ERP/service/customer_view.html',context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def approve_service(request , pk):
    vehicals = Vehical.objects.filter(customer = Customer.objects.get(user=request.user))
    service = Service.objects.get(id=pk)
    print('Ser', service.vehical in vehicals)
    if service.vehical in vehicals:
        service.is_approved = True
        service.save()
    return redirect('approve_estimate' , pk)
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def approve_estimate(request , pk):
    service = Service.objects.get(id = pk)
    vehicals = Vehical.objects.filter(customer = Customer.objects.get(user=request.user))
    if service.vehical in vehicals:
        try :
            estimate = Estimate.objects.get(service = service)
            context = {'estimate' : estimate}
            return render(request , 'ERP/estimate/approve_estimate_page.html' , context)
        except Exception as e:
            print(e)
            return render(request , 'ERP/estimate/not_ready.html')

    else:
        return redirect('unauth_page')
# Customer Service Updates
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def service_updates(request, pk):
    context = {}
    updates = Update.objects.filter(service = pk)
    context['updates'] = updates
    return render(request,'ERP/service/customer_update_view.html',context)
#  Employee Service Updates
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def employee_service_updates(request,pk):
    context = {}
    if request.method == 'POST':
        try :
            service = Service.objects.get(id = pk)
            form = UpdateForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                update = form.save(commit=False)
                update.service = service
                update.save()
                return redirect('employee_service_list')
            else :
                print('Not valid')
                return redirect('employee_service_update_page')
        except Exception as e:
            print(e)
            return redirect('employee_service_update_page')
    context['form'] = UpdateForm()

    return render(request,'ERP/service/employee_update_form.html',context)
# Employee Views :- 
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def add_service(request):
    employee = Employee.objects.get(user = request.user)
    center = employee.center
    if request.method == 'POST':
        try :
            print('1')
            
            vehical = Vehical.objects.get(id = request.POST['vehical'])
            
            print('2')
            print('Center = '+ str(center))
            service_ids = request.POST['services']
            services = []
            for id in service_ids:
                services.append(CenterServices.objects.get(id=id))
            additional_services = request.POST['add_services']
        
           
            service = Service.objects.create(
                vehical=vehical,
                #service_time = service_time,
                #service_date = datetime.datetime.strptime(service_date, "%Y-%m-%d").date(),
                center = center,
                progress = Service.Progress.WAITING,
                additional_services = additional_services,
                )

            
            service.save()
            service.services.set(services)
            return redirect('employee_service_list')
        except Exception as e:
            print('-------------------------------------------------------------------------------')
            print(e)
            return redirect('home_page')
    services = CenterServices.objects.filter(center = center)
    vehicals = Vehical.objects.all()
    context = {'services':services,
    'vehicals' : vehicals
    }
    return render(request , 'ERP/service/add.html' , context)
#

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def employee_service_list(request):
    context = {}
    employee = Employee.objects.get(user = request.user ) 
    services = list(Service.objects.filter(center = employee.center))
    print(services)
    context['services'] = services
    return render(request , 'ERP/service/employee_list.html', context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def update_progress(request,pk):
    #print(pk)
    context = {}   
    if request.method == 'POST':
        try :
            progress = request.POST['progress']
            service = Service.objects.get(id = pk)
            print(progress)
            service.progress = progress
            service.save()
            return redirect('employee_service_list')
        except Exception as e:
            print(e)
            return redirect('progress_update_page')
    form = UpdateProgressForm()
    context['form'] = form
    return render(request , 'ERP/service/progress_form.html' , context)

# Admin Only Views
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.ADMIN])
def approve_page(request):
    admin = Employee.objects.get(user = request.user)
    employees = Employee.objects.filter(center = admin.center)
    context = {'employees' : employees}
    return render(request , 'ERP/HR/approve_page.html' , context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.ADMIN])
def activate_employee(request , pk):
    employee = Employee.objects.get(id = pk)
    employee.user.is_active = True
    employee.user.save()
    return redirect('approve_page')

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.ADMIN])
def deactivate_employee(request , pk):
    employee = Employee.objects.get(id = pk)
    employee.user.is_active = False
    employee.user.save()
    return redirect('approve_page')
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.ADMIN])
def change_role(request , pk):
    employee = Employee.objects.get(id = pk)
    if request.method == 'POST':
        try :
            role = request.POST['role']
            employee.user.role = role
            employee.user.save()
            messages.info(request , 'Role Changed Succesfully')
            return redirect('change_role' , pk)
        except Exception as e :
            print(e)
            messages.info(request , 'Something Went Wrong ' + str(e))
            return redirect('change_role' , pk)

    context = {
        'employee' : employee,
        'form' : RoleForm()
    }

    return render(request , 'ERP/HR/change_role_page.html',context)
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN , User.Role.CUSTOMER])
def dashboard(request):
    if request.user.role == User.Role.CUSTOMER:
        return render(request ,'ERP/dashboard/customer.html')
    if request.user.role == User.Role.EMPLOYEE:
        return render(request ,'ERP/dashboard/employee.html')
    if request.user.role == User.Role.ADMIN:
        return render(request ,'ERP/dashboard/admin.html')
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def estimates(request):
    context = {}
    employee = Employee.objects.get(user = request.user)
    services = Service.objects.filter(center = employee.center)
    estimates = list(Estimate.objects.filter(service__in = services))
    context['estimates'] = estimates
    return render(request , 'ERP/estimate/estimates_view.html',context=context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def genrate_estimate(request , pk):

    service = Service.objects.get(id = pk)
    print(service)
    file_name = os.path.join(BASE_DIR ,MEDIA_ROOT , 'media' , 'estimates' ,f'{str(service.id)}{str(service.vehical)}.pdf')
    table_data = [['Name' , 'Price' , 'Tax' , 'Total']]
    for ser in list(service.services.all()):
        tot = ser.price * ((100 + ser.tax)/100)
        x = [ser.name , ser.price , ser.tax , tot]
        table_data.append(x)
    tot = service.additional_services_cost * 1.05
    x = [service.additional_services , service.additional_services_cost , '5' , tot]
    table_data.append(x)
    print(table_data)
    make_report(table_data=table_data , file_name=file_name , center_name=str(service.center))
    try :
        new_estimate = Estimate.objects.create(service = service , report = file_name)
        new_estimate.save()
        return redirect('estimates')
    except :
        messages.error(request , 'Only one estimate can be genrated for a service.')
        return redirect('employee_service_list')
    
   
    

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def delete_estimate(request , pk):
    estimate = Estimate.objects.get(id = pk)
    estimate.service.is_approved = False
    estimate.service.save()
    estimate.delete()
    return redirect('estimates')
   

  
    