from django.shortcuts import render , redirect
from .forms import BookingForm
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
    context ={}
    context['form']= BookingForm()
    return render(request,'Base/home.html',context=context)

def about(request):
    return render(request,'Base/aboutus.html')

def services(request):
    return render(request,'Base/service_page.html')

def booking(request):
    return render(request,'Base/booking_page.html')