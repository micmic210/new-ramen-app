from django.contrib import admin
from .models import Admin, Menu, ContactMessage, Table, Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'reservation_date', 'reservation_time', 'guests', 'status')
    search_fields = ['user__username', 'reservation_date', 'status']
    list_filter = ('status', 'reservation_date')

    # Obtain username of 'user'
    def get_user_name(self, obj):
        return obj.user.name if obj.user else None
    get_user_name.short_description = 'User Name' 

admin.site.register(Admin)
admin.site.register(Menu)
admin.site.register(ContactMessage)
admin.site.register(Table)
admin.site.register(Reservation, ReservationAdmin)
