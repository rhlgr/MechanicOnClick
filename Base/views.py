from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Base/home.html')

def about(request):
    return render(request,'Base/aboutus.html')

def services(request):
    return render(request,'Base/service_page.html')

def booking(request):
    return render(request,'Base/booking_page.html')