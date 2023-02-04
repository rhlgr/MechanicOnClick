from django.shortcuts import render , redirect
from .forms import BookingForm , ContactForm
from .models import Brand , VehicalModel , Booking
from django.contrib import messages


# Create your views here.
def get_context():
    context = {}
    booking_form = BookingForm()
    brands = Brand.objects.all()
    context['booking_form'] = booking_form
    context['contact_form'] = ContactForm
    context['brands'] = brands
    
    return context
#htmx Helper funtion
def get_models(request):
    brand = request.GET.get('brands')
    print('here')
    print(brand)
    models = VehicalModel.objects.filter(brand = brand)
    context = {'models' : models}

    return render(request , 'Base/partial/models.html' , context)
# @login_required(login_url= 'customer_login')
# @allowed_users(allowed_roles=[User.Role.CUSTOMER])
def home(request):
    
    if request.method == 'POST':
        try :
            print('In home post method')
            model = VehicalModel.objects.get(id = request.POST.get('model'))
            fuel =  request.POST.get('fuel')
            issue = request.POST.get('request')
            phone = request.POST.get('phone')
            print(fuel , issue , model , phone)
        
            x = Booking.objects.create(model=model ,phone = phone , fule_type = fuel , issue = issue)
            x.save()
            messages.info(request ,'Your booking was added succefully our team wil contact you shortly')
            return redirect('home_page')
        except Exception as e:
            print(e)
            messages.error(request ,'Something went wrong please make sure you entered all details correctly and try again')
            return redirect('home_page')
    context = get_context() 
    return render(request,'Base/home.html', context=context)
def service(request):
    return render(request ,'Base/service.html')
def unauth_error(request):
    return render(request,'error/unauthorized.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid:
            print('The form is Valid')
            try :
                form.save()
                print('saved')
                
                return redirect('home_page')
            except :
                #messages.error(request, 'Invalid Credentials')
                print('not saved')
                return redirect('home_page')
        else :
             print('The form is Not Valid')
    context = get_context()
    return render(request ,'Base/contact.html',context)