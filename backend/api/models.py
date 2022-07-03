from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)

class Status(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    postedAt=models.DateTimeField(auto_now=True)
    content=models.TextField(blank=False)