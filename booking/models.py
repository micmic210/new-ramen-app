from django.db import models
from django.contrib.auth import get_user_model
import random
import string
from django.contrib.auth.models import AbstractUser

#  User Model
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

# Table Model
class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True, null=False)
    capacity = models.PositiveIntegerField(null=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

# Reservation Model
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
        ('pending', 'Pending'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservations")
    email = models.EmailField(blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations", default=1)  
    reservation_date = models.DateField(null=False)
    reservation_time = models.TimeField(null=False)
    num_people = models.PositiveIntegerField(null=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='confirmed')
    created_at = models.DateTimeField(auto_now_add=True)
    special_request = models.TextField(blank=True, null=True)

    reservation_number = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.reservation_number:
            self.reservation_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            super().save(*args, **kwargs)


    def __str__(self):
        return f"Reservation {self.id} by {self.user.username} on {self.reservation_date} at {self.reservation_time}"

# Admin Model    
class Admin(models.Model):
    ROLE_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ]

    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

# Menu Model
class Menu(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="menus")

    def __str__(self):
        return self.name

# Contact Message
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


