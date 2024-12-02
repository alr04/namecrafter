from django.db import models
from django.conf import settings  # I’m importing settings for AUTH_USER_MODEL

class UserActionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # I’m ensuring this points to settings.AUTH_USER_MODEL
    action = models.CharField(max_length=255)  # I’m storing a description of the user action.
    timestamp = models.DateTimeField(auto_now_add=True)  # I’m recording when the action occurred.

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"  # I’m returning a string representation of the log entry.