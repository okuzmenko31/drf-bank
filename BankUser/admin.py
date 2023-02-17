from django.contrib import admin
from .models import BankUser


@admin.register(BankUser)
class BankUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['id', 'username', 'email']
    search_fields = ['id', 'username', 'email']
    list_filter = ['id', 'username', 'email']
