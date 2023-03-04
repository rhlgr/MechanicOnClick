from django.shortcuts import render , redirect
from .models import Customer , User , Employee 
from django.contrib import messages
from django.contrib.auth.models import auth
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
                    messages.error(request ,'Something Went Wrong!')
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
            try :
                auth.login(request, user)
                return redirect('dashboard')
            except :
                messages.error(request , "You are not authorized Yet Please Contact Admin")
            return redirect('login_page')
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
        #emp_img = request.POST['emp_img'] 
        try :
            if password1 == password2:
                user = User.objects.create_user(username=username ,role = User.Role.NA, password = password1 , phone = phone , first_name = first_name , last_name = last_name)
                user.save()
                print("done")
                #location = "Bhopal"
                try :
                    employee = Employee.objects.create(user = user , center = center)
                    employee.save()
                    messages.info(request, 'You can login  if authorized By Your Local Admin')
                    return redirect('login_page')
                except Exception as e :
                    print(e)
                    user.delete()
                    messages.error(request, 'Something Went Wrong')
                    return redirect('employee_register')
            else :
                 messages.error(request, 'Make sure you enter correct password in both fields.')
                 return redirect('employee_register')
            
        except :
            messages.error(request, 'Something Went Wrong')
            return redirect('employee_register')
    else :
        centers = Center.objects.all()
        context['centers'] = centers
        return render(request , 'account/employee_register.html' , context=context)

