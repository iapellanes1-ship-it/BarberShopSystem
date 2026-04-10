from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("client", "barber_name", "service_type", "date", "timeslot", "created_at")
    list_filter = ("barber_name", "service_type", "date")
    search_fields = ("client__username", "barber_name", "service_type")
