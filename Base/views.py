from django.shortcuts import render , redirect
from .forms import BookingForm 
from account.models import User
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required


# Create your views here.
def get_context():
    context = {}
    
    return context

@login_required(login_url= 'customer_login')
@allowed_users(allowed_roles=[User.Role.CUSTOMER])
def home(request):
    if request.method == 'POST':
        print('In home post method')
        form = BookingForm(request.POST)
        if form.is_valid:
            print('The form is Valid')
            try :
                form.save()
                
                return redirect('about_page')
            except :
                #messages.error(request, 'Invalid Credentials')
                return redirect('booking_page')
        else :
             print('The form is Not Valid')
    
    context = get_context() 
    return render(request,'Base/home.html', context=context)

def unauth_error(request):
    return render(request,'error/unauthorized.html')