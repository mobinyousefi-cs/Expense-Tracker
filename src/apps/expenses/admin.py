from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "kind", "category", "amount")
    list_filter = ("kind", "category", "date")
    search_fields = ("category", "notes")