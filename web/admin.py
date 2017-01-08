from django.contrib import admin
from .models import SchoolUser, Room, Reservation


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('login', 'room', 'date', 'time', 'note', 'is_blocked')


class SchoolUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'function')


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(SchoolUser, SchoolUserAdmin)



