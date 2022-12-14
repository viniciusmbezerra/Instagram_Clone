from django.contrib import admin

from .models import Comment, Like, Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    ...


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
