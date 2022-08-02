import email
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView , LogoutView


from . import forms
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'account/login.html'


class UserRegistrationView(generic.FormView):
    form_class = forms.UserCreationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('chat:direct_message')
    
    def form_valid(self, form):
        info_user = form.cleaned_data
        user = get_user_model().objects.create_user(
            full_name = info_user['full_name'],
            phone_number = info_user['phone_number'],
            email =  info_user['email'],
            password = info_user['password2'],
        )
        login(self.request , user)
        return super().form_valid(form)

# class RegisterView(View):
#     User = get_user_model()
#     form_class = forms.UserCreationForm
#     template_name = 'account/registeration.html'
#     def get(self , request):
#         form = self.form_class()
#         return render(request , self.tempalte_name , {'form':form})

#     def post(self , request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             info_user = form.cleaned_data
#             user = self.User.objects.create_user(
#                 full_name = info_user['full_name'],
#                 phone_number = info_user['phone_number'],
#                 password = info_user['password2'],
#             )
#             login(request , user)
#         return render(request , self.tempalte_name , {'form':form})


class UserLogoutView(LogoutView):
    pass
