from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('phone_number', 'full_name' , 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('full_name', 'password')}),
        ('Personal info', {'fields': ('phone_number','email' , 'profile_image')}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'full_name' , 'email' ,'phone_number' , 'profile_image', 'password1', 'password2'),
        }),
    )
    search_fields = ('full_name','email' ,'phone_number')
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)