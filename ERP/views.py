from django.shortcuts import render , redirect
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm
from account.models import User , Customer , Employee
from .models import Vehical , ProvidedService ,Service , Update

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
            return redirect('add_vehical_page')

    return render(request , 'ERP/vehical/add_vehical_page.html' , context)

@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def edit_vehical(request):
    user = request.user
    #print(user)
    customer = Customer.objects.get(user = user)
    vehicals = list(Vehical.objects.filter(customer = customer))
    #print(vehicals)
    context = {'vehicals' : vehicals}
    if request.method == 'POST':
        try :
            user = request.user
            #print(user)
            customer = Customer.objects.get(user = user)
            vehical_id = request.POST['vehical']
            vehicalnumber = request.POST['vehicalnumber']
            vehicaltype = request.POST['vehicaltype']
            print('info 1 :',vehicaltype , vehicalnumber , vehical_id)
            vehical =  Vehical.objects.get(id = 1)
            if len(vehicalnumber) == 0:
                vehicalnumber = vehical.number
            if len(vehicaltype) == 0:
                vehicaltype = vehical.type
            print('info 2 :',vehicaltype , vehicalnumber , vehical_id)
            vehical.number = vehicalnumber
            vehical.type = vehicaltype
            vehical.save()
        except Exception as e :
            print(e)
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


def approve_service(request , pk):
    vehicals = Vehical.objects.filter(customer = Customer.objects.get(user=request.user))
    service = Service.objects.get(id=pk)
    print('Ser', service.vehical in vehicals)
    if service.vehical in vehicals:
        service.is_approved = True
        service.save()
    return redirect('customer_service_page')
# Customer Service Updates
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def service_updates(request, pk):
    context = {}
    updates = Update.objects.filter(service = pk)
    context['updates'] = updates
    return render(request,'ERP/service/customer_update_view.html',context)
############### Employee Service Updates
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE])
def employee_service_updates(request,pk):
    context = {}
    if request.method == 'POST':
        try :
            update_image = request.POST['update_image']
            update_title = request.POST['update_title']
            update_description = request.POST['update_description']
            
            update = Update.objects.create(update_image = update_image , update_description = update_description , update_title = update_title , service = Service.objects.get(id = pk))
            return redirect('add_service_page')
        except Exception as e:
            print(e)
            return redirect('employee_service_update_page')
    context['form'] = UpdateForm()

    return render(request,'ERP/service/employee_update_form.html',context)
# Employee Views :- 
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.EMPLOYEE,User.Role.ADMIN])
def add_service(request):
    print('hi')
    if request.method == 'POST':
        print('here 1')
        try :
            employee = Employee.objects.get(user = request.user)
           
            vehical = Vehical.objects.get(id = request.POST['vehical'])
           
            service_time = request.POST['service_time']
           
            service_date = request.POST['service_date']
            service_estimate = request.POST['estimate']
            center = employee.center
            service_ids = request.POST['services']
            new_services = []
            for id in service_ids:
                new_services.append(ProvidedService.objects.get(id=id))
            additional_services = request.POST['add_services']
            additional_service_cost = request.POST['add_price']
            print(type(service_date) , service_date)
            service = Service.objects.create(
                vehical=vehical,
                #service_time = service_time,
                #service_date = datetime.datetime.strptime(service_date, "%Y-%m-%d").date(),
                center = center,
                progress = 'RO Open',
                
                additional_services = additional_services,
                additional_services_cost = additional_service_cost
                )

            print('here 1')
            service.save()
            service.services.set(new_services)
            print('here 5')
        except Exception as e:
            print('he')
            print(e)
            return redirect('home_page')
    services = ProvidedService.objects.all()
    vehicals = Vehical.objects.all()
    context = {'services':services,
    'vehicals' : vehicals
    }
    return render(request , 'ERP/service/add.html' , context)