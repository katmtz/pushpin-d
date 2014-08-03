from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Location(models.Model):
	# name, longitude, latitude should not be changed
	name = models.CharField(max_length=70)
	longitude = models.DecimalField(max_digits=7,decimal_places=4)
	latitude = models.DecimalField(max_digits=7,decimal_places=4)

	# editable fields that the user can choose to use
	custDescription = models.CharField(max_length=500, default='')
	custName = models.CharField(max_length=70, default='')

	# each Location is linked to one user to allow custom names
	# note: this is not really efficient memory-wise?? bc
	# lots of users = lots of duplicate locations
	user = models.ForeignKey(User)
	saveDate = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		if self.custName != '':
			return self.custName
		else:
			return self.name

	def getCoordinates(self):
		if (type(self.longitude) != str) and (type(self.latitude) != str):
			return "(" + str(self.longitude)+ ", " + str(self.latitude) + ")"
		else:
			return None
	getCoordinates.admin_order_field = 'name'
	getCoordinates.short_description = 'Coordinates'

	def isRecent(self):
		now = timezone.now()
		return now - datetime.timedelta(hours=12) <= self.saveDate <= now
