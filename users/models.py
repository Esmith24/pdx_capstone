from django.db import models
from django.contrib.auth.models import AbstractUser  # User
# Create your models here.


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


# class Profile(models.model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # def __str__(self):
        # return f'{self.user.username} Profile'
