from django.db import models
# social/models.py

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name='social_user_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # other fields

class Reply(models.Model):
    user = models.ForeignKey(User, related_name='social_user_replies', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # other fields

# Create your models here.
