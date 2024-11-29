from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReservationForm
from django.http import HttpResponse
from .models import Reservation


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

def contact(request):
    return render(request, 'contact.html')

    
