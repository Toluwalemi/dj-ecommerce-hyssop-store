from django.contrib import admin

# Register your models here.
from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email',
        'address', 'postal_code', 'city',
        'transport', 'created', 'status'
    ]
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]
