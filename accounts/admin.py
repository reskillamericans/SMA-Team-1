from django.contrib import admin
from .models import Users, User_Socials, Password_Resets
# Register your models here.

admin.site.register(Users)
admin.site.register(User_Socials)
admin.site.register(Password_Resets)