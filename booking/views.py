from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from django.http import HttpResponse
from .models import Reservation


def home(request):
    return render(request, 'home.html')

def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save() 
            form.save_m2m()
            return redirect('success')

    else:
        form = ReservationForm(initial={'user': request.user})
    
    return render(request, 'booking/reservation.html', {'form': form})


def confirm_reservation(request, reservation_number):
    reservation = get_object_or_404(Reservation, reservation_number=reservation_number)
    return render(request, 'booking/confirmation.html', {'reservation': reservation})


def cancel_reservation(request, reservation_number):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Get the reservation by reservation_number and email
        reservation = get_object_or_404(Reservation, reservation_number=reservation_number, email=email)

        reservation.status = 'canceled'
        reservation.save()

        return HttpResponse(f"Your reservation with number {reservation_number} has been successfully canceled.")

    return render(request, 'booking/confirmation.html')
