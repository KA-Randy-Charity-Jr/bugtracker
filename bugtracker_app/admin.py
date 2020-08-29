from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from bugtracker_app.models import MyUser


admin.site.register(MyUser, UserAdmin)