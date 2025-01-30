from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Room {self.id}"


class RoomParticipant(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name="participants", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        if self.sender:
            return f"{self.sender.username} (User)"
        return f"{self.content} (Mehmon)"


class Attachment(models.Model):
    message = models.ForeignKey(Message, related_name="attachments", on_delete=models.CASCADE)
    file_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class GuestUser(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
