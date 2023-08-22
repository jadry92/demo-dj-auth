""" User Model """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model.
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        """
        Return username.
        """
        return self.username

class Profile(models.Model):
    """
    User profile model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='users/avatar', blank=True, null=True)

    def __str__(self):
        """
        Return username.
        """
        return self.user.username