import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatRoom, Message, User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        
        await sync_to_async(Message.objects.create)(
            chat_room_id = 2,
            # sender_id = 1,
            # sender=self.scope["user"],
            content=message,
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "chat_message", "message": message},
        )

    async def chat_message(self, event):
        message = event["message"]
        # username = event["username"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
