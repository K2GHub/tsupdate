import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thought_sync.settings")
django.setup()

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Synch, SynchMembership, UserProfile

User = get_user_model()

from channels.consumer import AsyncConsumer

# class HomeConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })

class HomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("it's connected here")
        self.group_name = 'home'

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')
        data = text_data_json.get('data')

        # Handle different actions
        if action == 'some_action':
            # Perform some action with the data
            response_data = {
                'response': 'Handled some_action',
                'data': data
            }
            await self.send_json(response_data)

        # Broadcast message to group if needed
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'group_message',
                'message': text_data_json
            }
        )

    async def group_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))
    
    async def send_json(self, data):
        # Send JSON data
        await self.send(text_data=json.dumps(data))