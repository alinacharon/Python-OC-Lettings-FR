from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile that extends the built-in Django User model.
    Each profile is associated with a single user and contains additional information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles_profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile, which is
        the username of the associated user.
        """
        return self.user.username
