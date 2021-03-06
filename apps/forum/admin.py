# -*- coding: utf-8 -*-
from django.contrib import admin
from forum.models import Forum, Thread, Post, Subscription, Category, LastRead

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', '_parents_repr')
    list_filter = ('groups',)
    ordering = ['parent', 'title']
    prepopulated_fields = {"slug": ("title",)}

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['author','thread']

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'latest_post_time')
    list_filter = ('forum',)

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Category)
admin.site.register(LastRead)

