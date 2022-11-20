from unicodedata import category

from rest_framework import serializers

from .models import (
    DimensionsValue,
    Category,
    Color,
    ColorImage,
    ColorPrice,
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
        fields = ("id", "name", "description", "image", "parent", "position")


class ProductImageSerializer(serializers.ModelSerializer):
    """Product Image"""

    class Meta:
        model = ProductImage
        fields = ("id", "image", "alt_text")


class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    """Product specification value"""

    specification = serializers.SlugRelatedField(
        slug_field="name", read_only=True)

    class Meta:
        model = ProductSpecificationValue
        fields = ("id", "specification", "value")


class ColorImageSerializer(serializers.ModelSerializer):
    """Color"""

    class Meta:
        model = ColorImage
        fields = ("id", "image", "alt_text", "is_active")


class ColorSerializer(serializers.ModelSerializer):
    """Color"""

    color_image = ColorImageSerializer(read_only=True, many=True)
    class Meta:
        model = Color
        fields = ("id", "name", "color_image")


class ColorPriceSerializer(serializers.ModelSerializer):
    """Color Price"""

    color = ColorSerializer(read_only=True)

    class Meta:
        model = ColorPrice
        fields = ("id", "color", "price_percent")


class DimensionsValueSerializer(serializers.ModelSerializer):
    """Dimensions Value"""

    dimension = serializers.SlugRelatedField(
        slug_field="name", read_only=True)

    class Meta:
        model = DimensionsValue
        fields = ("id", "value", "dimension", "price_change")


class ProductDetailSerializer(serializers.ModelSerializer):
    """Product"""

    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )
    product_image = ProductImageSerializer(many=True)
    product_specification_value = ProductSpecificationValueSerializer(many=True)
    color_price = ColorPriceSerializer(many=True)
    dimensions_value = DimensionsValueSerializer(many=True)

    class Meta:
        model = Product
        exclude = ("is_active",)


class ProductListSerializer(serializers.ModelSerializer):
    """Products list"""

    category = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True
    )
    product_image = ProductImageSerializer(many=True)
    product_specification_value = ProductSpecificationValueSerializer(many=True)
    color_price = ColorPriceSerializer(many=True)
    dimensions_value = DimensionsValueSerializer(many=True)

    class Meta:
        model = Product
        exclude = ("is_active",)
