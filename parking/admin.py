from django.contrib import admin

from .models import Watchman, Vehicle, VehicleType, Client, Ticket

admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(Watchman)
admin.site.register(Client)
admin.site.register(Ticket)
