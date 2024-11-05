from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='login_user_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='login_user_permissions_set', 
        blank=True,
        help_text='Specific permissions for this user.'
    )
