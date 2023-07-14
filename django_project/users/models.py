from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        resize_to = (300,300)

        if self.image.height>300 or self.image.width>300:
            img.thumbnail(resize_to)
            img.save(self.image.path)


