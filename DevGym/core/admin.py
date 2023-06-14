from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'hour')  # Campos a mostrar en la lista de reservas

admin.site.register(Reservation, ReservationAdmin)
