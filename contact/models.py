from django.db import models
from core.models import AbstractModel
# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default='',
        max_length=100,
        blank=True,
        verbose_name='Name',
    )
    email = models.EmailField(
        default='',
        verbose_name='Email',
        blank=True,
        max_length=254,
    )
    subject = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Subject',
    )
    message = models.TextField(
        default='',
        verbose_name='Message',
        blank=True,
    )
    def __str__(self):
        return f'Message:{self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('name',)