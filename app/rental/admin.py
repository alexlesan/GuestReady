from django.contrib import admin

from .models import (Rental, Reservation)

class RentalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = []
    list_filter = []
    fieldsets = []    


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['rental', 'title', 'checkin', 'checkout']
    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(Rental, RentalAdmin)
admin.site.register(Reservation, ReservationAdmin)
