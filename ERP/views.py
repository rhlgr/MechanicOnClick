from django.shortcuts import render , redirect
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from account.models import User , Customer
from .models import Vehical
# Create your views here.
@login_required(login_url= 'customer_login')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def add_vehical(request):
    context = {}
    if request.method == 'POST':
        try :
            print('Here 1')
            user = request.user
            print('Here 2')
            customer = Customer.objects.get(user = user)
            print(customer)
            vehicalnumber = request.POST['vehicalnumber']
            print('Here 4')
            vechicaltype = request.POST['vehicaltype']
            print('Here 5')
            new_vehcial =  Vehical.objects.create(customer = customer , number = vehicalnumber , type = vechicaltype)
            print('Here 6')
            new_vehcial.save()
            print('Here 7')
        except Exception as e:
            print(e)
            return redirect('add_vehical_page')

    return render(request , 'ERP/vehical/add_vehical_page.html' , context)

@login_required(login_url= 'customer_login')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def edit_vehical(request):
    user = request.user
    #print(user)
    customer = Customer.objects.get(user = user)
    vehicals = list(Vehical.objects.filter(customer = customer))
    print(vehicals)
    context = {'vehicals' : vehicals}
    if request.method == 'POST':
        try :
            user = request.user
            print(user)
            customer = Customer.objects.get(user = user)
            vehicalnumber = request.POST['vehicalnumber']
            vechicaltype = request.POST['vehicaltype']
            new_vehcial =  Vehical.objects.create(customer = customer , number = vehicalnumber , type = vechicaltype)
            new_vehcial.save()
        except :
            return redirect('edit_vehical_page')
    return render(request , 'ERP/vehical/edit_vehical_page.html' , context)