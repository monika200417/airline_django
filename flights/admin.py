from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Flight , Airport, Passenger
# Register your models here.

class FlightAdmin(ModelAdmin):
    list_display=("id", "origin", "destination", "duration")

class PassengerAdmin(ModelAdmin):
    filter_horizontal=("flights",)
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
