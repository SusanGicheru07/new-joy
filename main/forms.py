from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Booking, Payment, Guest, Room, RoomType

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'check_in_date', 'check_out_date']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'mpesa_code']
        widgets = {
             'payment_method': forms.RadioSelect(attrs={'required': True}),
            'mpesa_code': forms.TextInput(attrs={'placeholder': 'Enter M-Pesa code here'}),
        }
    
class GuestForm(forms.ModelForm):
    id = forms.IntegerField(help_text="Enter the guest's ID")
    payment_method = forms.CharField(max_length=10)
    choices=[('mpesa', 'MPESA'), ('cash', 'Cash')],
    label='Payment Method',
    widget=forms.RadioSelect
    payment_amount = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(500), MaxValueValidator(1000)],
        label='Payment Amount'
    )

    class Meta:
        model = Guest
        fields = ['id', 'name', 'payment_amount', 'payment_method']



        
