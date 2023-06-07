from django.contrib import admin

from .models import Conversation, ConversationMessage


# Register your models here.
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id',  )

class ConversationMessageAdmin(admin.ModelAdmin):
    list_display = ('id', )
    
    
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(ConversationMessage, ConversationMessageAdmin)

