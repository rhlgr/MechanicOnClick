from django.shortcuts import render , redirect
from .forms import BookingForm , ContactForm
from account.models import Employee
from .models import Testimonial
from ERP.models import ProvidedService
# Create your views here.
def get_context():
    context = {}
    employees = Employee.objects.filter(on_display = True)
    testimonials = Testimonial.objects.filter(on_display = True)
    provided_services = ProvidedService.objects.filter(on_display = True)
    print("Hello")
    print(testimonials.values())
    context['employees'] = employees
    context['testimonials'] = testimonials
    context['provided_services'] = provided_services
    return context

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

def about(request):
    context = get_context()
    return render(request,'Base/aboutus.html' , context=context)

def services(request):
    context = get_context()
    return render(request,'Base/service_page.html', context=context)

def booking(request):
    if request.method == 'POST':
        print('In BOOKING post method')
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
    return render(request,'Base/booking_page.html' , context=context)

def contact(request):
    if request.method == 'POST':
        print('In Contact post method')
        form = ContactForm(request.POST)
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
    return render(request,'Base/contact_page.html',context=context)