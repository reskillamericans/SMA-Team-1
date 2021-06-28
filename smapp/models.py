from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(unique = True)
    is_email_verified = models.BooleanField()
    password = models.CharField(max_length = 255)
    status = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255, default = 'user')
    bio = models.CharField(max_length = 255)
    occupation = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    followers_count = models.IntegerField(default = 0, null = True)
    following_count = models.IntegerField(default = 0, null = True)
    profile_picture = models.ImageField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    def _str__(self):
        return self.first_name + self.last_name

class User_Followers(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    #follower_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    is_post_notification_subscribed = models.BooleanField()
    status = models.BooleanField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Password_Resets(models.Model):
    user_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    token = models.CharField(max_length = 255)
    is_token_used = models.BooleanField()
    expired_at = models.DateTimeField(default = None)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class User_Socials(models.Model):
    user_id = models.OneToOneField(Users, on_delete = models.PROTECT)
    facebook_link = models.CharField(max_length = 255)
    github_link = models.CharField(max_length = 255)
    linkedin_link = models.CharField(max_length = 255)
    instagram_link = models.CharField(max_length = 255)
    twitter_link = models.CharField(max_length = 255)
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
    sender_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    #recipient_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    read_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
