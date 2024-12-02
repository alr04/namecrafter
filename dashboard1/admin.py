from django.contrib import admin
from .models import UserActionLog  # I’m importing the UserActionLog model to register it in the admin interface.

# # I’m registering the UserActionLog model to make it accessible in the admin interface.
admin.site.register(UserActionLog)