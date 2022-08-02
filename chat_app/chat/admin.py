import imp
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ['sender' , 'receiver' , 'message_body']