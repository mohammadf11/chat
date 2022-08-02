from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/' , views.UserLoginView.as_view() , name = 'login'),
    path('registration/' , views.UserRegistrationView.as_view() , name = 'registration'),
    path('logout/' , views.UserLogoutView.as_view() , name = 'logout')
]