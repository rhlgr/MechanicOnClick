from django.forms import ModelForm
from .models import Booking , Contact

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'