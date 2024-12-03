from django.contrib import admin
from .models import CustomUser, ToDoItems


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'name')
    search_fields = ('username', 'email', 'name')


@admin.register(ToDoItems)
class ToDoItemsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'due_date', 'status')
    search_fields = ('user', 'title', 'description', 'due_date', 'status')
    list_filter = ('status', 'due_date')
