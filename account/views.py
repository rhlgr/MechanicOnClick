from django.shortcuts import render , redirect
from .models import Customer , User , Employee ,EmployeeAdmin
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib import messages
from ERP.models import Center
# Create your views here.
def customer_register(request):
    context ={}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        location = request.POST['location']
        try :
            if password1 == password2:
                user = User.objects.create_user(username=username,is_active =True ,role = User.Role.CUSTOMER, password = password1 , phone = phone , first_name = first_name , last_name = last_name)
                user.save()
                print("done")
                #location = "Bhopal"
                try :
                    customer = Customer.objects.create(user = user , location = location)
                    customer.save()
                    return redirect('login_page')
                except :
                    user.delete()
                    return redirect('customer_register')
            
        except :
            return render(request, 'account/register.html' , context=context)
    else :
        return render(request , 'account/register.html' , context=context)

def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username , password)
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else :
            print('Login Failed')
            messages.error(request , "Invalid Credentials")
            return redirect('login_page')
    else :
        return render(request , 'account/login.html')

def customer_logout(request):
    auth.logout(request)
    return redirect('login_page')

# Employee Register

def employee_register(request):
    context ={}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        center = Center.objects.get(id =request.POST['center'])
        emp_img = request.POST['emp_img'] 
        try :
            if password1 == password2:
                user = User.objects.create_user(username=username ,role = User.Role.EMPLOYEE, password = password1 , phone = phone , first_name = first_name , last_name = last_name)
                user.save()
                print("done")
                #location = "Bhopal"
                try :
                    employee = Employee.objects.create(user = user , center = center , emp_img = emp_img)
                    employee.save()
                    return redirect('login_page')
                except :
                    user.delete()
                    return redirect('employee_register')
            
        except :
            return redirect('employee_register')
    else :
        centers = Center.objects.all()
        context['centers'] = centers
        return render(request , 'account/employee_register.html' , context=context)
# Employee Register

def admin_register(request):
    context ={}
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        center = Center.objects.get(id =request.POST['center'])
        emp_img = request.POST['emp_img'] 
        try :
            if password1 == password2:
                user = User.objects.create_user(username=username ,role = User.Role.ADMIN, password = password1 , phone = phone , first_name = first_name , last_name = last_name)
                user.save()
                print("done")
                #location = "Bhopal"
                try :
                    print('Trying')
                    employee = EmployeeAdmin.objects.create(user = user , center = center , emp_img = emp_img)
                    employee.save()
                    print('Hurray')
                    return redirect('login_page')
                except Exception as e :
                    print(e)
                    user.delete()
                    return redirect('employee_admin_register')
                
        except Exception as e :
            print('Oops')
            print(e)
            return redirect('employee_admin_register')
    else :
        centers = Center.objects.all()
        context['centers'] = centers
        return render(request , 'account/employee_register.html' , context=context)