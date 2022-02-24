from django.contrib import admin

# Register your models here.
from .models import Ticket, Reservation


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    fields = [
        'flight', 'num_people', 'total_cost'
    ]
    inlines = [TicketInline]


admin.site.register(Reservation, ReservationAdmin)
