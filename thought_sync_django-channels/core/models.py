from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""
"""
class User (AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(unique=True)
# end of User model 



