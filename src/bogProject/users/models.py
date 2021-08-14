from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePicture = models.ImageField(upload_to='profilePicture', default='myProfile.png')
    about = models.TextField(default='about me')


    def __str__(self) -> str:
        return f'{self.user.username} profile'
