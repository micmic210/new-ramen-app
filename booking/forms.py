from django import forms
from .models import Reservation, Table
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'reservation_date', 'reservation_time', 'guests', 'special_request']
        widgets = {
    
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'reservation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Guests'}),
            'special_request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any special requests (optional)', 'rows': 3}),
        }
    
    def clean_reservation_time(self):
        reservation_time = self.cleaned_data['reservation_time']
        if reservation_time < datetime.time(12, 0) or reservation_time > datetime.time(21, 0):
            raise forms.ValidationError("Please select a time between 12:00 and 21:00.")
        return reservation_time


    def save(self, commit=True):
        reservation = super().save(commit=False)

        reservation.user = self.initial.get('user', None)

        if commit:
            reservation.save()
            self.save_m2m()
        return reservation
