from unicodedata import category

from rest_framework import serializers

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
)


class ParentCategoryFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryListSerializer(serializers.ModelSerializer):
    """List of product categories"""

    # parent = serializers.SlugRelatedField(slug_field="name", read_only=True)
    parent = ParentCategoryFilterSerializer(read_only=True)
    # children = ChildrenCategoryFilterSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "slug", "parent", "position", "is_active")


class ProductListSerializer(serializers.ModelSerializer):
    """Product"""

    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )

    class Meta:
        model = Product
        exclude = ("is_active",)


class ProductDetailSerializer(serializers.ModelSerializer):
    """Product"""

    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )

    class Meta:
        model = Product
        exclude = ("is_active",)
