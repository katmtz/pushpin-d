Pushpin'd

Pushpin'd is a webapp designed to allow users to save and organize physical places that they deem notable (ie. restaurants, museums, photo-op spots). Currently, these locations must be manually saved with a name, longitude/latitude, and description. The next step is to use Google's Maps API to integrate the location saving functionality with a more user-friendly means of identifying places. Later plans include better sharing capabilities, both between users on the site and possibly via facebook. 

Things used to make pushpin'd better:
-Django
-Bootstrap
-jQuery (duh)

Pushpin'd Project Directory:

pushpin/

	locationlib/ (app)
		static/
			locationlib/
				boostrap.min.css
				bootstrap.min.js

		templates/
			locationlib/
				new.html
				index.html
				edit.html
				detail.html
		__init__.py
		admin.py
		forms.py
		models.py
		tests.py
		urls.py
		views.py

	pushpin/
		__init__.py
		forms.py
		settings.py
		urls.py
		views.py
		wsgi.py

	static/
		bootstrap.min.css
		bootstrap.min.js
		style.css

	templates/ 
		admin/
			base_site.html
		home.htmls
		login.html
		signup.html

	users/ (app)
		templates/
			users/
				edit.html
				index.html
				profile.html

		__init__.py
		admin.py
		models.py
		tests.py
		urls.py
		views.py

	db.sqlite.sqlite3
	manage.py
	README.txt

Pushpin Views:
- "home" page: landing page for site, links to useful things, login/sign up
- "signup" page: displays form for creating new user (email, username, password)
- "login" page: displays form for authenticating user (view: userLogin())
- "about" page: info about this site, usage
- "contact" page: info about me
- "authenticator" action: calls authenticate(), redirects to success landing page
- "success" page: refer to user "profile" page
- "createNew" action: saves new user account


Users (app:users) Views:
- User "profile" page: displays profile information about user
	- Profile "edit" page: displays form to edit profile information
	- Profile "save" action: saves changes to user profile
- User "places" page: displays list of saved locations + (*)map
	- (*)Places "autoadd" action: pulls form data from map, saves as new location
	- Places "add" page: displays form for manual location addition
	- Places "edit" page: displays list of locations with deletion option
	- Places "save" action: refer to location "save" action
	- Places "savenew" action: refer to location "savenew" action

Location Library (app:locationlib) Views:
- Location "index" page: displays all created locations (to be repurposed)  
- Location "detail" page: displays information about a particular location
- Location "edit" page: displays form for changes in an existing location
- Location "new" page: displays form for manual creation of location
- Location "savenew" action: handles creation of new user location 
- Location "save" action: handles changes to existing location
- Location "delete" action: handles location deletion

(*) Custom Error Views:
- 404
- 500
- 403
- bad request

(*) still working on this

Notes:
This is a work in progress and a personal project and as such, there's plenty of bugs and errors I haven't gotten around to. There's also lots of debugging print statements, and a few comments that might be less than professional, but hopefully I'll have all that sorted out eventually.