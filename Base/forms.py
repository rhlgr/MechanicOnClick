from django.forms import ModelForm
from .models import Booking , Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'