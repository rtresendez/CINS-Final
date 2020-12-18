from django.db import models
import re
from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.

class Story_Model(models.Model):
    story = models.CharField(max_length=240)

    def __str__(self):
        return self.story

class chartRoomModel(models.Model):
    roomName = models.CharField(max_length=36)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_file = models.FileField(upload_to="uploaded_files")

    def __str__(self):
        return self.roomName + " by: " + self.user.username + " for: " + self.upload_file.name