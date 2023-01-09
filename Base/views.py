from django.shortcuts import render , redirect
from .forms import BookingForm , ContactForm
from account.models import Employee
from .models import Testimonial ,CarasouleElement
from ERP.models import ProvidedService
# Create your views here.
def get_context():
    context = {}
    
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

