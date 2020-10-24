from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('test', self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({'message': 'Connected to server!', 'username': 'SERVER'}))

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)('test', self.channel_name)

        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        async_to_sync(self.channel_layer.group_send)(
            'test',
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    def chat_message(self, event):
        message = event['message']
        username = event['username']

        self.send(text_data=json.dumps({'message': message, 'username': username}))
