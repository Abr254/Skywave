from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    # Other fields can be added here

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Message(models.Model):
    user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} to {self.recipient.username}: {self.content}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='user_posts/videos/', blank=True, null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return f'{self.user.username} - {self.caption}'

class MediaItem(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='media/')
    type = models.CharField(max_length=10, choices=MEDIA_TYPES)

    def __str__(self):
        return self.title