import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone
from .models import Conversation, Message


class ConversationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_id = self.scope["url_route"]["kwargs"]["conversation_id"]
        user = self.scope.get("user")
        if not user or not user.is_authenticated or not await self.is_participant(user.pk):
            await self.close(code=4403)
            return
        self.group_name = f"conversation_{self.conversation_id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        try:
            payload = json.loads(text_data or "{}")
            body = str(payload.get("body", "")).strip()
            if not body or len(body) > 4000:
                await self.send_json({"type": "error", "message": "Message must contain 1–4000 characters."})
                return
            saved = await self.save_message(self.scope["user"].pk, body)
            if not saved:
                await self.close(code=4403)
                return
            await self.channel_layer.group_send(self.group_name, {"type": "chat.message", "message": saved})
        except (ValueError, TypeError, json.JSONDecodeError):
            await self.send_json({"type": "error", "message": "Invalid message payload."})

    async def chat_message(self, event):
        await self.send_json(event["message"])

    @database_sync_to_async
    def is_participant(self, user_id):
        return Conversation.objects.filter(pk=self.conversation_id).filter(
            buyer_id=user_id
        ).exists() or Conversation.objects.filter(pk=self.conversation_id, seller_id=user_id).exists()

    @database_sync_to_async
    def save_message(self, user_id, body):
        try:
            conversation = Conversation.objects.select_related("buyer", "seller").get(pk=self.conversation_id)
        except Conversation.DoesNotExist:
            return None
        if user_id not in (conversation.buyer_id, conversation.seller_id):
            return None
        now = timezone.now()
        message = Message.objects.create(conversation=conversation, sender_id=user_id, body=body)
        Conversation.objects.filter(
            pk=conversation.pk, first_message_at__isnull=True
        ).update(first_message_at=message.created_at)
        Conversation.objects.filter(pk=conversation.pk).update(updated_at=now)
        return {"type": "message", "id": message.pk, "body": message.body,
                "sender_id": user_id, "sender": message.sender.username,
                "created_at": message.created_at.isoformat()}
