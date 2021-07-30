from django.db import models
from accounts.models import Users

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
    sender_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    #recipient_id = models.ForeignKey(Users, on_delete = models.PROTECT)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    read_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()



class User(models.Model):
    name = models.CharField(max_length=40)
    pwd = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Followers(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    another_user = models.ManyToManyField(Users, related_name='another_user')

    def __str__(self):
        return self.users.name


