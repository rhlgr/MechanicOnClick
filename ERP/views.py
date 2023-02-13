from django.shortcuts import render , redirect
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm , UpdateProgressForm , PaySlipForm
from account.models import User , Customer , Employee
from .models import Vehical  ,Service , Update , CenterServices , Estimate , PaySlip
from django.contrib import messages
from .reports import make_report
import os
from account.forms import RoleForm
from MOC.settings import MEDIA_ROOT , BASE_DIR
#Employee Service Updates

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
            vehical = Vehical.objects.get(number = request.POST['vehical'])
            print('Center = '+ str(center))
            service_ids = request.POST['services']
            services = []
            for id in service_ids:
                services.append(CenterServices.objects.get(id=id))
            additional_services = request.POST['add_services']
            additional_services_cost = request.POST['add_ser_amt']
        
           
            service = Service.objects.create(
                vehical=vehical,
                #service_time = service_time,
                #service_date = datetime.datetime.strptime(service_date, "%Y-%m-%d").date(),
                center = center,
                progress = Service.Progress.WAITING,
                additional_services = additional_services,
                additional_services_cost = additional_services_cost
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
@allowed_users(allowed_roles=[User.Role.ADMIN])
def show_pay_slips(request , pk):
    employee = Employee.objects.get(id = pk)
    slips = PaySlip.objects.filter(employee = employee)
    context = {
        'slips' : slips,
        'emp_id' : pk,
        }

    return render(request , 'ERP/HR/pay_slips_page.html',context)
    
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.ADMIN])
def add_pay_slip(request , pk):
    context = {}
    employee = Employee.objects.get(id = pk)
    admin = Employee.objects.get(user = request.user)
    context['emloyee'] = admin
    if employee.center == admin.center:
        if request.method == 'POST':
            try :
                form = PaySlipForm(request.POST, request.FILES)
                
                slip = form.save(commit=False)
                print('Hi')
                slip.employee = employee
                slip.save()
                return redirect('pay_slips' , pk)
            except Exception as e:
                print('exe')
                print(e)
                messages.error(request , "Something Went Wrong")
                return redirect('add_pay_slip' , pk)
        context['form'] = PaySlipForm()
        return render(request , 'ERP/HR/add_pay_slip.html' , context)
    else:
        return redirect('unauth_page')

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
    total_estimate = 0
    for ser in list(service.services.all()):
        tot = ser.price * ((100 + ser.tax)/100)
        total_estimate += tot
        x = [ser.name , ser.price , ser.tax , tot]
        table_data.append(x)
    # Adding Additional Services Cost with 5% GST
    tot = service.additional_services_cost * 1.05
    total_estimate += tot
    x = [service.additional_services , service.additional_services_cost , '5' , tot]
    table_data.append(x)
    x = ['', '' ,'Total' , total_estimate]
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
   

  
    