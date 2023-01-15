from rest_framework import serializers

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class PostListSerializer(serializers.ModelSerializer):
    """List of posts"""

    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ("status", "created", "updated")


class PostDetailSerializer(serializers.ModelSerializer):
    """Post"""

    category = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Post
        exclude = ("status", "created", "updated")
