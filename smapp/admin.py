from django.contrib import admin
from .models import Post_Comments, Post_Likes, Posts, Categories, Messages, User, Followers

# Register your models here.
admin.site.register(Post_Comments)
admin.site.register(Post_Likes)
admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Messages)
admin.site.register(User)
admin.site.register(Followers)

