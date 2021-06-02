from django.contrib import admin
from .models import Profile, FriendRequest, Chat

admin.site.register(Profile)
admin.site.register(FriendRequest)
admin.site.register(Chat)