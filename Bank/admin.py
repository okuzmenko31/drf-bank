from django.contrib import admin
from .models import TransferCategory, Transfer, BankAccount, Transaction, Customer


@admin.register(TransferCategory)
class TransferCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'from_account', 'to_account']
    list_display_links = ['id', 'category', 'to_account']
    search_fields = ['id', 'category', 'from_account', 'to_account']
    list_filter = ['id', 'category', 'from_account', 'to_account']


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'account_number', 'balance']
    list_display_links = ['id', 'account_number']
    list_editable = ['user']
    search_fields = ['id', 'user', 'account_number', 'balance']
    list_filter = ['id', 'user', 'account_number']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'transfer', 'user']
    list_display_links = ['id']
    list_editable = ['category']
    search_fields = ['id', 'category', 'transfer', 'user']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'country', 'city']
    list_display_links = ['id', 'first_name', 'last_name', 'country', 'city']
    list_editable = ['user']
    search_fields = ['id', 'user', 'first_name', 'last_name', 'country', 'city']
    list_filter = ['id', 'first_name', 'last_name', 'country', 'city', 'user']

