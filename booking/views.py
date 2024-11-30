from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail 
from .forms import ReservationForm
from django.http import HttpResponse
from .models import Reservation
from django import forms


def home(request):
    return render(request, 'home.html')

def philosophy(request):
    return render(request, 'philosophy.html')

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save() 
            form.save_m2m()

            return redirect('confirm_reservation', reservation_number=reservation.reservation_number)

    else:
        form = ReservationForm(initial={'user': request.user})
    
    return render(request, 'booking/reservation.html', {'form': form})


def confirm_reservation(request, reservation_number):

    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    return render(request, 'booking/confirmation.html', {'reservation': reservation})


# Contact Form Definition
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'})
    )

# Contact View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']  
            message = form.cleaned_data['message']

            # Send an email 
            send_mail(
                f"Contact Form Submission from {name}",  
                message,  
                'inouem888@gmail.com',  
                ['minoue@globalbizsupport.com'],  
                fail_silently=False,
            )

            return render(request, 'thank_you.html')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



   
