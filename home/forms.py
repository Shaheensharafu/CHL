from django import forms
from .models import booking

class date_input(forms.DateInput):
    input_type='date'

class bookingform(forms.ModelForm):
    class Meta:
        model=booking
        fields='__all__'
        
        widgets={
            'booking_date':date_input(),
        }

        labels={
            'p_name': 'Patient Name:',
            'p_phone': 'Patient Phone',
            'p_email':'Patient E-mail',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date',
        }