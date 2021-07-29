from django.db import models
from accounts.models import Users
from django.conf import settings

class User_Followers(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    #follower_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    is_post_notification_subscribed = models.BooleanField()
    status = models.BooleanField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Categories(models.Model): 
    created_by = models.ForeignKey(Users, on_delete = models.PROTECT)
    cat_type = models.CharField(max_length = 255)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Posts(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    category_id = models.ForeignKey(Categories, on_delete = models.PROTECT)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    likes_count = models.IntegerField(default = 0, null = True)
    comments_count = models.IntegerField(default = 0, null = True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Post_Comments(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    post_id = models.ForeignKey(Posts, on_delete = models.PROTECT)
    content = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Post_Likes(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    post_id = models.ForeignKey(Posts, on_delete = models.PROTECT)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Messages(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="message_sender", on_delete=models.DO_NOTHING)
    #sender_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="message_receiver", on_delete=models.DO_NOTHING)
    #recipient_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    read_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
