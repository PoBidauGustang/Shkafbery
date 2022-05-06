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


class SchemeFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillingScheme
        fields = ["id", "name"]


class DimensionsSerializer(serializers.ModelSerializer):

    filling_scheme = SchemeFilterSerializer(read_only=True)

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

    filling_scheme = SchemeFilterSerializer(read_only=True, many=True)

    class Meta:
        model = BodyColour
        fields = ["id", "filling_scheme", "name", "image", "alt_text"]


class DoorsSystemSerializer(serializers.ModelSerializer):

    filling_scheme = SchemeFilterSerializer(read_only=True, many=True)

    class Meta:
        model = DoorsSystem
        fields = ["id", "name", "position", "filling_scheme", "description"]


class DoorsSystemFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorsSystem
        fields = ["id", "name"]


class DoorsProfilesSerializer(serializers.ModelSerializer):

    doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

    class Meta:
        model = DoorsProfiles
        fields = ["id", "name", "image", "doors_system", "description", "alt_text"]


class DoorhandleSerializer(serializers.ModelSerializer):

    doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

    class Meta:
        model = Doorhandle
        fields = ["id", "name", "image", "doors_system", "description", "alt_text"]


class DoorsMaterialsSerializer(serializers.ModelSerializer):

    doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

    class Meta:
        model = DoorsMaterials
        fields = ["id", "name", "image", "doors_system", "description", "alt_text"]
