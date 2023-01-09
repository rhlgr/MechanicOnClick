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
            user = request.user
            customer = Customer.objects.get(user = user)
            vehicalnumber = request.POST['vehicalnumber']
            vechicaltype = request.POST['vehicaltype']
            new_vehcial =  Vehical.objects.create(customer = customer , number = vehicalnumber , type = vechicaltype)
            new_vehcial.save()
        except :
            return redirect('add_vehical_page')
            
    return render(request , 'ERP/add_vehical_page.html' , context)
def edit_vehical(request):
    context = {}
    if request.method == 'POST':
        try :
            user = request.user
            customer = Customer.objects.get(user = user)
            vehicalnumber = request.POST['vehicalnumber']
            vechicaltype = request.POST['vehicaltype']
            new_vehcial =  Vehical.objects.create(customer = customer , number = vehicalnumber , type = vechicaltype)
            new_vehcial.save()
        except :
            return redirect('add_vehical_page')
    return render(request , 'ERP/vehical/add_vehical_page.html' , context)