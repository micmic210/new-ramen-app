from django.contrib import admin
from .models import Admin, Menu, ContactMessage, Table, Reservation

admin.site.register(Admin)
admin.site.register(Menu)
admin.site.register(ContactMessage)
admin.site.register(Table)
admin.site.register(Reservation)
