from django.contrib import admin
from .models import Admin, Menu, ContactMessage, Table, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reservation_date', 'reservation_time', 'status', 'created_at')
    search_fields = ['user__username', 'reservation_date', 'status']
    list_filter = ('status', 'reservation_date')

admin.site.register(Admin)
admin.site.register(Menu)
admin.site.register(ContactMessage)
admin.site.register(Table)
admin.site.register(Reservation, ReservationAdmin)
