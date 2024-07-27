from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoomType(models.Model):
    TYPE_A = 'A'
    TYPE_B = 'B'

    TYPES_CHOICES = [
        (TYPE_A, 'Class A'),
        (TYPE_B, 'Class B'),
    ]
    name = models.CharField(max_length=1, choices=TYPES_CHOICES, primary_key=True)

    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.get_room_type_display()} {self.room_number}"
    
class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    room_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Room {self.room_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, default='A')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - Room {self.room.room_number} ({self.check_in_date} to {self.check_out_date})"

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    PAYMENT_METHODS = (
        ('MPESA', 'M-Pesa'),
        ('CASH', 'Cash'),
    )
    payment_method = models.CharField(max_length=5, choices=PAYMENT_METHODS)
    mpesa_code = models.CharField(max_length=255, blank=True, null=True)
    
    transaction_id = models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking}"
    
class Guest(models.Model):
    
    #id = models.AutoField(primary_key=True)
    manual_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    check_in_time = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=6, decimal_places=2)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name