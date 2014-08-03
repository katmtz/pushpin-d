from django.contrib import admin
from users.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['firstName','lastName','about','user']}),
	]

	list_display = ('user', 'firstName', 'lastName')

admin.site.register(Profile, ProfileAdmin)