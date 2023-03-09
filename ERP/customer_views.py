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
  
    vehical = Vehical.objects.get(number = pk)
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
@login_required(login_url= 'login_page')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def vehical_services(request , pk):
    vehical = Vehical.objects.get(id = pk)
    #services = Service.objects.filter(vehical = vehical)
    customer = Customer.objects.get(user = request.user)
    if customer == vehical.customer:
        context = {}
        app_services = Service.objects.filter(is_approved = True , vehical = vehical)
        #app_services = Service.objects.filter(is_approved = True )
        not_app_services = Service.objects.filter(is_approved = False, vehical = vehical)
        context['app_services'] = app_services
        context['not_app_services'] = not_app_services
        return render(request , 'ERP/service/customer_view.html',context)

    else:
        return redirect('unauth_page')
