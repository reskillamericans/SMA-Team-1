from django.db import models
from accounts.models import Users
from django.conf import settings

class User_Followers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    #follower_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    is_post_notification_subscribed = models.BooleanField()
    status = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Categories(models.Model):
    cat_type = models.CharField(max_length=255, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cat_type

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['cat_type']

class Posts(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    category_id = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes_count = models.IntegerField(default=0, null=True)
    comments_count = models.IntegerField(default=0, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['user_id']

class Post_Comments(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    post_id = models.ForeignKey(Posts, on_delete=models.PROTECT)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Comments"
        ordering = ['created_at']

class Post_Likes(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    post_id = models.ForeignKey(Posts, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Likes"
        ordering = ['post_id']

class Messages(models.Model):
    sender_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="message_sender", on_delete=models.DO_NOTHING)
    #sender_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    receiver_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="message_receiver", on_delete=models.DO_NOTHING)
    #recipient_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    title = models.CharField(max_length = 255)
    content = models.TextField()
    read_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ['created_at']
