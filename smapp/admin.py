from django.contrib import admin
from .models import Users, User_Followers, User_Socials, Password_Resets, Post_Comments, Post_Likes, Posts, Categories, Messages

# Register your models here.
admin.site.register(Users)
admin.site.register(User_Followers)
admin.site.register(User_Socials)
admin.site.register(Password_Resets)
admin.site.register(Post_Comments)
admin.site.register(Post_Likes)
admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Messages)