from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from locationlib.models import Location
from users.models import Profile
from users.forms import ProfileForm

def verifyUser(request, requestedUser): # helper function
	# checks whether the remote user matches the user_id in url
	currentUser = request.user
	return currentUser == requestedUser

def profile(request, user_id): # page
	# displays info about particular user
	user = get_object_or_404(User, pk=user_id)
	userProfile = Profile.objects.get(user=user) 
	context = {
		'user':user,
		'profile':userProfile,
		'request':request,
	}
	return render(request, 'users/profile.html', context) 

def edit(request, user_id): # page
	# displays form to edit profile
	user = get_object_or_404(User, pk=user_id)
	verifyUser(request, user)
	userProfile = Profile.objects.get(user=user)
	form = ProfileForm()
	context = {
		'profile':userProfile, 
		'user':user, 
		'form':form,
	}
	return render(request, 'users/edit.html', context)

def save(request, user_id): # action
	# saves changes to user profile
	user = get_object_or_404(User, pk=user_id)
	userProfile = Profile.objects.get(user=user)
	if request.method == 'POST':
		form = ProfileForm(request.POST,instance=userProfile)
		if form.is_valid():
			print form
			form.save()
			print "form saved!"
			return HttpResponseRedirect(reverse('users:profile', args=[user_id]))
		else:
			
			return HttpResponseRedirect(reverse('users:edit', args=[user_id]))

def places_index(request,user_id):
	user = get_object_or_404(User, pk=user_id)
	userProfile = Profile.objects.get(user=user)
	location_list = userProfile.get_locations()
	context = {
		'user':user,
		'profile':userProfile,
		'location_list':location_list,
		'request':request
	}
	return render(request, 'users/index.html', context)

def add(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	return HttpResponseRedirect(reverse('locationlib:new'))
	
