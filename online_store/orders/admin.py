from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "full_name",
        "email",
        "address",
        "town",
        "phone",
        "total_order_price",
        "payment_option",
        "billing_status",
    ]
    list_editable = ["billing_status",]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order",
        "product",
        "dimensions",
        "color",
        "price",
        "quantity",

    ]
