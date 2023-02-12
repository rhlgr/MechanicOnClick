from django.shortcuts import render , redirect
from .forms import ContactForm
from .models import Brand , VehicalModel , Booking
from django.contrib import messages


# Create your views here.
def get_context():
    context = {}
    context['contact_form'] = ContactForm
    
    return context
#htmx Helper funtion
def get_models(request):
    brand = request.GET.get('brands')
    print('here')
    print(brand)
    models = VehicalModel.objects.filter(brand = brand)
    context = {'models' : models}

    return render(request , 'Base/partial/models.html' , context)
def get_brands(request):
    type = request.GET.get('type')
    if type == '1':
        brands = Brand.objects.filter(has_two_wheeler = True)
    elif type == '2':
        brands = Brand.objects.filter(has_four_wheeler = True)
    context = {'brands' : brands}
    return render(request , 'Base/partial/brands.html' , context)
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
            #print(fuel , issue , model , phone)
        
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
        form = ContactForm(request.POST)
        if form.is_valid():
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

def test(request):

    return render(request,'dashboard.html')