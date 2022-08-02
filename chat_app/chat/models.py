from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(get_user_model() , on_delete=models.CASCADE , related_name='mesasges1' )
    receiver = models.ForeignKey(get_user_model() , on_delete=models.CASCADE, related_name='mesasges2' )
    message_body = models.CharField(max_length=255)
    file = models.FileField(upload_to='message_file/' , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created']