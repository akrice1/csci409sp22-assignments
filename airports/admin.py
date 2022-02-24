from django.contrib import admin
from .models import Airport, Runway


# Register your models here
class RunwayInline(admin.StackedInline):
    model = Runway  # specify which model to use
    extra = 2  # how many to start with


class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'airport_code', 'is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'], 'classes': ['collapse']})
    ]
    inlines = [RunwayInline]  # load the RunwayInline Class


admin.site.register(Airport, AirportAdmin)
