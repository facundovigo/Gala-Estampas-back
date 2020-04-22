from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Event


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'event_picture')
