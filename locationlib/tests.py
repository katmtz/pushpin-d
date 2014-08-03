from django.test import TestCase
from locationlib.models import Location
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime

superuser = User.objects.get(username='katherine')

# Create your tests here.
class LocationMethodTests(TestCase):

	def testGetCoordinates(self):
		# should not crash for any input
		print 'Testing getCoordinates:' 
		print '-Testing nonnumerical inputs...',
		nonnumCoords = Location()
		(nonnumCoords.longitude,nonnumCoords.latitude) = ('ha','ha')
		self.assertEqual(nonnumCoords.getCoordinates(), None)
		print 'Passed!'

		print '-Testing expected inputs...',
		correctCoords = Location()
		(correctCoords.longitude,correctCoords.latitude) = (34.4566,-118.9653)
		self.assertEqual(correctCoords.getCoordinates(), "(34.4566, -118.9653)")
		print 'Passed!'

		print 'All tests passed!'

	def testIsRecent(self):
		print 'Testing isRecent:'
		now = timezone.now()

		print "-Testing past date...",
		pastLocation = Location()
		pastLocation.saveDate = now - datetime.timedelta(days=1)
		self.assertEqual(pastLocation.isRecent(), False)
		print "Passed!"

		print "-Testing recent date...",
		recentLocation = Location()
		recentLocation.saveDate = now - datetime.timedelta(hours=5)
		self.assertEqual(recentLocation.isRecent(), True)
		print "Passed!"

		print "-Testing future date...",
		futureLocation = Location()
		futureLocation.saveDate = now + datetime.timedelta(days=1)
		self.assertEqual(futureLocation.isRecent(), False)
		print "Passed!"

		print "All tests passed!"

class LocationViewTests(TestCase):
	def create_location(self, name='', user=superuser,
	 longitude=12.3456,latitude=-123.456, custName='', custDescription='',dateOffset=0):
		return Location.objects.create(
			name=name,
			user=user,
			longitude=longitude,
			latitude=latitude,
			custName=custName,
			custDescription=custDescription,
			saveDate=timezone.now() + datetime.timedelta(days=dateOffset),
			)

	def delete_location(self, name):
		l = Location.objects.get(name=name)
		l.delete()

	def testIndexView(self):
		print "Testing index view:"
		# should display only 5 recent locations
		

		print "-testing with no locations...",
		# should display "No places saved!"
		response = self.client.get(reverse('locationlib:index'))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertContains(response, "No places saved!")
		self.assertQuerysetEqual(response.context['location_list'], [])
		print "Passed!"

		print "-testing with past location...",
		# location should be in location_list
		self.create_location(name='loc', dateOffset=-30)
		response = self.client.get(reverse('locationlib:index'))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertQuerysetEqual(
			response.context['location_list'],
			['<Location: loc>']
			)
		print "Passed!"
		self.delete_location('loc')

		print "-testing with future location...",
		# location_list should be empty
		self.create_location(name='loc', dateOffset=2)
		response = self.client.get(reverse('locationlib:index'))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertQuerysetEqual(response.context['location_list'], [])
		print "Passed!"
		self.delete_location('loc')

		print "-testing with future location and 5 recent locations...",
		# only recent locations should be in list
		for i in xrange(5):
			namestr="loc"+"i"*(i+1)
			self.create_location(name=namestr)
		self.create_location(name='loc', dateOffset=2)
		response = self.client.get(reverse('locationlib:index'))
		self.assertEqual(response.status_code,200)
		print "view status: OK...",
		self.assertEqual(len(response.context['location_list']), 5)
		self.assertNotContains(response, "<Location: loc>")
		print "Passed!"
		self.delete_location('loc')

		print "-testing with >5 locations...",
		# only 5 most recent locations should  show
		for i in xrange(4):
			namestr = "loc" + "j"*(i+1)
			self.create_location(name=namestr)
		response = self.client.get(reverse('locationlib:index'))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertNotContains(response, '<Location: lociii>')
		print "Passed!"

		print "All tests passed!"

	def testDetailView(self):
		print "Testing detail view:"
		
		print "-testing with custom name...",
		# should display custom name as subheading
		self.create_location(name="loc", custName="my loc")
		loc = Location.objects.get(name='loc')
		response = self.client.get(reverse('locationlib:detail', args=[loc.id]))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertContains(response, '<h3>my loc</h3>')
		print "Passed!"

		print "-testing custom description...",
		# custom description should be displayed
		self.create_location(
			name='loc2', 
			custDescription="A nice description.",
			)
		loc = Location.objects.get(name="loc2")
		response = self.client.get(reverse('locationlib:detail', args=[loc.id]))
		self.assertEqual(response.status_code,200)
		print "view status: OK...",
		self.assertContains(response,"A nice description.")
		print "Passed!"

		print "-testing hide description...",
		# if no custom description, description label should not be displayed
		self.create_location(name='loc3')
		loc = Location.objects.get(name="loc3")
		response = self.client.get(reverse('locationlib:detail', args=[loc.id]))
		self.assertEqual(response.status_code, 200)
		print "view status: OK...",
		self.assertNotContains(response, "Description")
		print "Passed!"

		print "All tests passed!"

	def testSaveAction(self):
		print "Testing save action:"
		print "never fucking mind I'm out"




