from django.contrib import admin
from .models import Todolist, Todo


class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'priority', 'is_published')
    list_display_links = ('id', 'title', 'priority', 'is_published')
    search_fields = ('title', 'id')
    prepopulated_fields = {"title": ("title",)}

admin.site.register(Todolist, TodolistAdmin)


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority')
    list_display_links = ('title', 'priority')
    search_fields = ('title', 'priority')
    prepopulated_fields = {"title": ("title",)}

admin.site.register(Todo, TodoAdmin)
