from rest_framework import serializers

from .models import (
    AdditionalElements,
    BodyColour,
    BodyComplectation,
    CategoryAdditionalElements,
    CategoryBodyComplectation,
    ClosetType,
    Dimensions,
    Doorhandle,
    DoorsColours,
    DoorsMaterials,
    DoorsProfiles,
    DoorsSystem,
    FillingScheme,
)


class ClosetTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClosetType
        exclude = ("is_active",)


# class PostListSerializer(serializers.ModelSerializer):
#     """List of posts"""

#     category = CategorySerializer(read_only=True, many=True)

#     class Meta:
#         model = Post
#         fields = "__all__"


# class PostDetailSerializer(serializers.ModelSerializer):
#     """Post"""

#     category = CategorySerializer(read_only=True, many=True)

#     class Meta:
#         model = Post
#         exclude = ("status",)
