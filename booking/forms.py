from django import forms
from .models import Reservation, Table
from django.contrib.auth import get_user_model

User = get_user_model()

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'reservation_time', 'num_people', 'special_request', 'table']

    reservation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Reservation Date")
    reservation_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label="Reservation Time")
    special_request = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Any special requests (e.g. allergies, children, etc.)'}), required=False, label="Special Requests")
    num_people = forms.IntegerField(min_value=1, label="Number of People")
    table = forms.ModelChoiceField(queryset=Table.objects.all(), label="Select Table")
    

    def save(self, commit=True):
        reservation = super().save(commit=False)

        reservation.user = self.initial.get('user', None)

        if commit:
            reservation.save()
            self.save_m2m()
        return reservation
