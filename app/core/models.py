"""
Database models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
# AbstractBaseUser provide features for authentication but doesn't include any field(we must define them)
# PermissionsMixin used for the Django permissions system. It includes field and methods that are needed for our user model.
# BaseUserManager, base class for managing users. Contains useful helper methods (normalize_email for exmaple) but we will also define our own methods..

class UserManager(BaseUserManager):
    """Manage for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    # AbstractBaseUser contains functionality for authentication but not any field.
    # PermissionsMixin contains functionality for the permissions and any fields needed for the permissions system.
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    # We are going to set this user as our custom user model in settings.py by adding AUTH_USER_MODEL = 'core.User'