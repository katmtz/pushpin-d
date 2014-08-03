from django.contrib import admin
from locationlib.models import Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name','user','saveDate']}),
		('Custom Information', {'fields':['custName', 'custDescription']}),
		('Coordinates', {'fields':['longitude','latitude'], 'classes':['collapse']}),
	]

	list_display = ('name', 'getCoordinates','user')

admin.site.register(Location, LocationAdmin)

