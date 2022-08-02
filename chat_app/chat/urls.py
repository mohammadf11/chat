from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('' , views.DirectMessage.as_view() , name = 'direct_message'),
    path('<int:user_id>' , views.DirectMessage.as_view() , name = 'direct_message'),
    path('edit_profile' , views.EditProfile.as_view() , name = 'edit_profile'),
]