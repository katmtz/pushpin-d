from django.forms import ModelForm
from locationlib.models import Location

class LocationForm(ModelForm):
	class Meta:
		model = Location
		fields = ['name', 'user','longitude','latitude','custDescription']