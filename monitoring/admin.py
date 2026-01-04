from django.contrib import admin

# Register your models here.

from .models import Capteur, Mesure, Ticket

admin.site.register(Capteur)
admin.site.register(Mesure)
admin.site.register(Ticket)
