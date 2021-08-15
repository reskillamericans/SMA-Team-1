from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class AccountStatus(models.TextChoices):
        LOCKED = 'Locked', 'Locked'
        UNLOCKED = 'Unlocked', 'Unlocked'
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(unique = True)
    is_email_verified = models.BooleanField(default = False)
    password = models.CharField(max_length = 255)
    status = models.CharField(max_length=10, choices=AccountStatus.choices, default=AccountStatus.UNLOCKED, null=True, blank=True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    bio = models.CharField(max_length = 255, null = True)
    occupation = models.CharField(max_length = 255, null = True)
    location = models.CharField(max_length = 255, null = True)
    followers_count = models.IntegerField(default = 0, null = True)
    following_count = models.IntegerField(default = 0, null = True)
    profile_picture = models.ImageField(null = True)
    last_login = models.DateTimeField(auto_now_add = True)
    date_joined = models.DateTimeField(auto_now_add = True)

    def _str__(self):
        return self.username


class User_Socials(models.Model):
    user_id = models.OneToOneField(Users, on_delete = models.PROTECT)
    facebook_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    github_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    linkedin_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    instagram_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    twitter_link = models.CharField(max_length=255, null=True, blank=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_id.username

    class Meta:
        verbose_name_plural = "User Socials"
        ordering = ['user_id']
    
class Password_Resets(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT)
    token = models.CharField(max_length=255, unique=True, null=True, blank=True, default=None)
    is_token_used = models.BooleanField(default=False)
    expired_at = models.DateTimeField(default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user_id.username

    class Meta:
        verbose_name_plural = "Password Resets"
        ordering = ['user_id']
