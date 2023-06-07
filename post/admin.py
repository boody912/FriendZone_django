from django.contrib import admin

from .models import Post, PostAttachment,Like,Trend




class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'created_at')

class PostAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_by')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'created_by', 'created_at_formatted', 'likes_count')

class TrendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'hashtag',  'occurences')


admin.site.register(Like, LikeAdmin)
admin.site.register(PostAttachment, PostAttachmentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Trend,TrendsAdmin)