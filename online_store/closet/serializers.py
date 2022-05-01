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
    DoorsMaterials,
    DoorsProfiles,
    DoorsSystem,
    FillingScheme,
)


class ClosetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosetType
        # fields = ["id", "type", "description"]
        exclude = ("is_active",)


class SchemeDimensionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillingScheme
        fields = ["id", "name"]


class DimensionsSerializer(serializers.ModelSerializer):

    filling_scheme = SchemeDimensionsSerializer(read_only=True)

    class Meta:
        model = Dimensions
        fields = "__all__"


class TypeSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosetType
        fields = ["type"]


class FillingSchemeSerializer(serializers.ModelSerializer):

    type = TypeSchemeSerializer(read_only=True)

    class Meta:
        model = FillingScheme
        exclude = ("is_active",)


class BodyColourSerializer(serializers.ModelSerializer):

    filling_scheme = SchemeDimensionsSerializer(read_only=True, many=True)

    class Meta:
        model = BodyColour
        fields = ["id", "filling_scheme", "name", "image", "alt_text"]
