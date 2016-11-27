from django.contrib import admin
from .models import Administrator, Room, Reservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('login', 'room', 'date', 'time', 'note', 'is_blocked')


class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('login', 'name')


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Administrator, AdministratorAdmin)



