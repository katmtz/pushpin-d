from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from locationlib.models import Location
from locationlib.forms import LocationForm

def index(request):
	# lists recent saved locations
	location_list = Location.objects.filter(
		saveDate__lte=timezone.now
	).order_by('-saveDate')[:5]
	context = {'location_list': location_list}
	return render(request, 'locationlib/index.html', context)

def new(request):
	form = LocationForm().as_p()
	context = {
		"form":form,
		"request":request,
	}
	return render(request, 'locationlib/new.html', context)
	
def detail(request, location_id):
	# displays info about particular location
	location = get_object_or_404(Location, pk=location_id)
	context = {
		'location':location,
		'user':location.user,
		'request':request,
	}
	return render(request, 'locationlib/detail.html', context)

def edit(request,location_id):
	# displays information edit form
	location = get_object_or_404(Location, pk=location_id)
	context = {
		'location':location,
		'request':request
	}
	return render(request, 'locationlib/edit.html', context)

def save(request, location_id):
	# saves changes from edit form
	l = get_object_or_404(Location, pk=location_id)
	# uses TRY/EXCEPT method.. switch to form.is_valid() later
	try:
		l.custName = request.POST['name']
		l.custDescription = request.POST['description']
	except (AttributeError):
		return render(request, 'locationlib:detail.html', {
			'location': l,
			'error_message': "Input not valid.", # use more descriptive err msg?
			})
	else:
		l.save()
		return HttpResponseRedirect(reverse('locationlib:detail', args=(l.id,)))

def savenew(request):
	# saves a new location
	print '**SAVENEW DEBUG LOG**'
	print 'savenew called'
	if request.method == 'POST':
		form = LocationForm(request.POST)
		print 'form set'
		if form.is_valid():
			newLocation = form.save()
			print 'form saved'
			print '**OK**'
			return HttpResponseRedirect(reverse('locationlib:detail', args=[newLocation.id]))
		print 'form invalid'
		print form
		print '**OK**'
		return render(request, 'locationlib/new.html', {'form': form})
	else:
		form = LocationForm()
		print 'form reset'
		print '**ERR:METHOD NOT POST**'
		return render(request, 'locationlib/new.html', {'form': form})

def delete(request, location_id):
	l = get_object_or_404(Location, pk=location_id)
	l.delete()
	return HttpResponseRedirect(reverse('users:places', args=[request.user.id]))