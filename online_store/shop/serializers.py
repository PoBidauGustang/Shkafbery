from unicodedata import category

from rest_framework import serializers

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
)


class CategoryListSerializer(serializers.ModelSerializer):
    """List of product categories"""

    parent = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "parent", "is_active")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Product"""

    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )

    class Meta:
        model = Product
        exclude = ("is_active",)
