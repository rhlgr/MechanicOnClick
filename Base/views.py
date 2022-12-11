from django.shortcuts import render , redirect
from .forms import BookingForm , ContactForm
# Create your views here.
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
  
 
    return render(request,'Base/home.html')

def about(request):
    return render(request,'Base/aboutus.html')

def services(request):
    return render(request,'Base/service_page.html')

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
    return render(request,'Base/booking_page.html')

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
    
    return render(request,'Base/contact_page.html')