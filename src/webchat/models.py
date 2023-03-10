from django.db import models
from django.urls import reverse

from user.models import Person



class Chat(models.Model):
    title = models.CharField(max_length=60)
    members = models.ManyToManyField(Person,  related_name='chats', )
    admin = models.ForeignKey(Person, blank=True, null=True, on_delete=models.PROTECT, related_name='admin')



    def __str__(self):
        return f"Chat {self.title}"

    def return_link(self):
        return reverse('chat-room', kwargs={'room_id': self.id})

    def last_message(self):
        msg = self.chat_messages.select_related('author').all().latest('timestamp')
        return msg if msg else 'Write your first words!'



class Message(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(Person, related_name='messages', on_delete=models.CASCADE,)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.timestamp}] {self.author}: {self.text}"









