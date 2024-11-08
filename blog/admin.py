from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'author', 'post_date')
    list_display_links = ('id', 'title', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'comment_date')
    list_display_links = ('id', 'post', )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
