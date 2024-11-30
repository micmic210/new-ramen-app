from django.contrib import admin
from .models import Admin, Menu, Table, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'reservation_date', 'reservation_time', 'guests', 'status')
    search_fields = ['name', 'email', 'phone', 'reservation_date', 'status']
    list_filter = ('status', 'reservation_date')


admin.site.register(Admin)
admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Reservation, ReservationAdmin)
