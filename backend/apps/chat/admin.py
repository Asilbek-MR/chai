from django.contrib import admin
from .models import ChatRoom,RoomParticipant,Message,Attachment

# Register your models here.

myModels = [ChatRoom,RoomParticipant, Message,Attachment] 
admin.site.register(myModels)
