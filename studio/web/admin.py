from django.contrib import admin
from .models import *

@admin.register(DesignCategory)
class DesignCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'subject', 'email', 'timestamp')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'email', 'category', 'timestamp')
    search_fields = ('user__username', 'fullname', 'email')  # Поиск по указанным полям

@admin.register(Executor)
class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'bio', 'skills')

@admin.register(ClientOrder)
class ClientOrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'assigned_executor', 'status', 'timestamp')
