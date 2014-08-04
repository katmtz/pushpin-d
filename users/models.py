from django.db import models
from django.contrib.auth.models import User
from locationlib.models import Location

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)
	firstName = models.CharField(max_length=50, blank=True, verbose_name="First Name")
	lastName = models.CharField(max_length=50, blank=True, verbose_name="Last Name")
	about = models.CharField(max_length=500, blank=True, verbose_name="About")

	def __unicode__(self):
		profileName = self.user.username + "_profile"
		return profileName

	def get_locations(self):
		# returns list of all locations related to user
		return Location.objects.filter(user=self.user)

	
