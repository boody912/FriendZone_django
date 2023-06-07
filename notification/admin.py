from django.contrib import admin
from .models import Notification
# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_of_notification', 'created_by', 'created_for', 'created_at', 'is_read')
    list_filter = ('type_of_notification', 'is_read')
    search_fields = ('type_of_notification', 'created_by__username', 'created_for__username')

admin.site.register(Notification, NotificationAdmin)