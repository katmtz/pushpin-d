from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from forms import NewUserForm
from locationlib.models import Location
from users.models import Profile

def home(request):
	loggedin = request.user.is_authenticated()
	context = {
		'loggedin':loggedin,
		'request':request
	}
	return render(request, 'home.html', context)

def signup(request):
	form = NewUserForm().as_ul()
	print form
	return render(request, 'signup.html', {'form':form})

def createUser(request):
	print "** createUser DEBUG LOG**"
	form = NewUserForm(request.POST)
	print 'form set'
	if form.is_valid():
		newUser = form.save()
		newUserProfile = Profile(user=newUser)
		newUserProfile.save()
		print "user '%s' created" % newUser.username
		print '**OK**'
		return HttpResponseRedirect(reverse('home'))
	else:
		form = NewUserForm()
		print 'form reset'
		print '**ERR FORM CREATION FAILED**'
		return render(request, 'signup.html', {'form':form})

def userLogin(request):
	return render(request, "login.html")

def authenticator(request):
	print "Authentication LOG:"
	username = request.POST['username']
	password = request.POST['password']
	print 'Authenticating user...'
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			print "LOG IN SUCESSFUL"
			return HttpResponseRedirect(reverse('users:profile', args=[user.id]))
		else:
			print "USER INACTIVE"
			HttpResponseRedirect(reverse('login'))
	else:
		print "INVALID CREDENTIALS"
		HttpResponseRedirect(reverse('login'))

def userLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))