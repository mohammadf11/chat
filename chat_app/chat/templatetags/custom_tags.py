from django import template
from chat.models import Message
from django.contrib.auth import get_user_model

register = template.Library()

@register.simple_tag(takes_context=True)
def get_last_message(context , user_id ):
        request = context['request']
        user = get_user_model().objects.get(id = user_id)
        messages1 = list(Message.objects.filter(sender = request.user , receiver = user))
        messages2 = list(Message.objects.filter(sender = user, receiver = request.user))
        if len(messages1 + messages2): 
            if len(messages2) == 0:
                 return messages1[-1].message_body[:15]
            elif len(messages1) == 0:
                 return messages2[-1].message_body[:15]
            elif messages1[-1].created <= messages2[-1].created:
                return messages2[-1].message_body[:15]
            else:
                return messages1[-1].message_body[:15]
        return ' '
    
    