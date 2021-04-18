from django.contrib.auth.models import User
from django.db import models

from Backend import settings


class Chat(models.Model):
    CHAT_TYPE_CHOICES = [
        ('D', 'Dialog'),
        ('C', 'Chat')
    ]

    type_chat = models.CharField(choices=CHAT_TYPE_CHOICES, max_length=1, verbose_name='Тип чата')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Участники')

    class Meta:
        db_table = 'Чат'
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        db_table = 'Сообщение'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
