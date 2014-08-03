from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from locationlib.models import Location
from users.models import Profile

def verifyUser(request, requestedUser): # helper function
	# checks whether the remote user matches the user_id in url
	currentUser = request.REMOTE_USER
	return currentUser == requestedUser

def profile(request, user_id): # page
	# displays info about particular user
	user = get_object_or_404(User, pk=user_id)
	userProfile = Profile.objects.get(user=user) 
	return render(request, 'users/profile.html', {'profile':userProfile,'user':user}) 

def edit(request, user_id): # page
	# displays form to edit profile
	user = get_object_or_404(User, pk=user_id)
	verifyUser(request, user)
	userProfile = Profile.objects.get(user=user)
	return render(request, 'users/edit.html', {'profile':userProfile, 'user':user})

def save(request, user_id): # action
	# saves changes to user profile
	pass

def places_index(request,user_id):
	user = get_object_or_404(User, pk=user_id)
	userProfile = Profile.objects.get(user=user)
	location_list = userProfile.get_locations()
	context = {
		'user':user,
		'profile':userProfile,
		'location_list':location_list,
	}
	return render(request, 'users/index.html', context)

def places_edit(request,user_id):
	pass

def add(request, user_id):
	pass