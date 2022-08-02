from cProfile import Profile
from django.shortcuts import render , redirect
from .models import Message
from django.views import View
from django.contrib.auth import get_user_model
from account.forms import ProfileForm
from .forms import MessageBarForm
# Create your views here.

class DirectMessage(View):
    template_name = 'chat/chat_page.html'
    form_calss = MessageBarForm
    
    def get(self , request , user_id=1 ):
        
        
        users = get_user_model().objects.all()
        user = users.get(id = user_id)
        messages1 = list(Message.objects.filter(sender = request.user , receiver = user))
        messages2 = list(Message.objects.filter(sender = user, receiver = request.user))
        messages = []
        for _ in range(len(messages1) + len(messages2)):
            if len(messages1) == 0:
                messages.append(messages2.pop(0))
            elif len(messages2) == 0:
                messages.append(messages1.pop(0))
            
            elif messages1[0].created <= messages2[0].created :
                messages.append(messages1.pop(0))
            else:
                messages.append(messages2.pop(0))
        
        
        context ={
            'direct_user' :user,
            'users':users,
            'messages':messages,
            'form':self.form_calss(),
            'profile_form' : ProfileForm(instance=request.user)
        }
        
        return render(request , self.template_name , context )

    def post(self , request , user_id):
        form = self.form_calss(request.POST)
        if form.is_valid():
            user =get_user_model().objects.get(id = user_id)
            Message.objects.create(
                sender = request.user ,
                receiver =user ,
                message_body = form.cleaned_data['message_bar']
                )
            return redirect('chat:direct_message' , user_id)
        return render(request , self.template_name , {"form":form} )


class EditProfile(View):
    def post(self , request):
        form = ProfileForm(request.POST , request.FILES , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('chat:direct_message' )
        