from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cms.models import GalacticUser

admin.site.register(GalacticUser, UserAdmin)
