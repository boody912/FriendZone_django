from django.contrib import admin

# Register your models here.
from .models import User, FriendshipRequest


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

admin.site.register(User, UserAdmin)

class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_for', 'created_at', 'created_by', 'status')
admin.site.register(FriendshipRequest, FriendshipRequestAdmin)
