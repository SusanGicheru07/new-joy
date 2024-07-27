from django.shortcuts import render,redirect
from .models import Payment, Booking, RoomType, Guest
from .forms import PaymentForm, BookingForm, GuestForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def booking_roomA(request):
    return booking(request, room_type='A')

def booking_roomB(request):
    return booking(request, room_type='B')

def booking(request, room_type=None):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room_type = room_type
            # Calculate total cost based on your business logic
            booking.total_cost = calculate_total_cost(booking)
            booking.save()
            # Optionally, redirect to a payment page or confirmation page
            return redirect('payment_page')  # Replace 'payment_page' with the actual URL name
    else:
        form = BookingForm(initial={'room_type': room_type})
    return render(request, 'booking_form.html', {'form': form})

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            if payment.payment_method == 'MPESA':
                # Simulate initiating the M-Pesa payment process
                # This is where you'd integrate with the M-Pesa API to initiate the payment
                # For now, we'll just redirect to a hypothetical confirmation page
                # You might also save the payment instance here after marking it as initiated
                payment.status = 'INITIATED'
                payment.save()
                return redirect('confirmation_page')
                
            else:
                # Mark the payment as pending
                payment.status = 'PENDING'
                payment.save()
                # Redirect to a page where users can confirm their cash payment details
                return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'guest_list.html', {'guests': guests})

def add_guest(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guest_list')
    else:
        form = GuestForm()
    return render(request, 'add_guest.html', {'form': form})

