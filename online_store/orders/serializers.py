from unicodedata import category

from rest_framework import serializers
from django.conf import settings
from .models import (
    Order,
    OrderItem,
)


# class ImageActiveSerializer(serializers.ListSerializer):
#     """Фильтр изображений, только active"""

#     def to_representation(self, data):
#         data = data.filter(is_active=True)
#         return super().to_representation(data)


# class ParentCategoryFilterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ["id", "name"]


# settings.AUTH_USER_MODEL


class OrderListSerializer(serializers.ModelSerializer):
    """List of orders"""

    # parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # parent = ParentCategoryFilterSerializer(read_only=True)
    # children = ChildrenCategoryFilterSerializer(read_only=True, many=True)

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        # exclude = ("created", "updated")
        fields = ['id', 'user', 'full_name', 'email', 'address', 'town', 'phone', 'total_order_price', 'payment_option', 'billing_status']

class UserSerializer(serializers.ModelSerializer):
    order_user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email', 'order_user']

class OrderSerializer(serializers.ModelSerializer):
    """Order"""

    # parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # parent = ParentCategoryFilterSerializer(read_only=True)
    # children = ChildrenCategoryFilterSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        exclude = ("created", "updated")


class OrderItemsSerializer(serializers.ModelSerializer):
    """OrderItems"""

    # parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # parent = ParentCategoryFilterSerializer(read_only=True)
    # children = ChildrenCategoryFilterSerializer(read_only=True, many=True)

    class Meta:
        model = OrderItem
        fields = ("id",)