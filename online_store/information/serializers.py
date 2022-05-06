from rest_framework import serializers

from .models import AboutCompany, Examples, ExamplesPhoto, Faq


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        exclude = ("is_active", "created_at", "updated_at")


class ExamplesFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examples
        fields = ["id", "name"]


class ExamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examples
        exclude = ("is_active", "for_main", "created_at", "updated_at")


class ExamplesPhotoSerializer(serializers.ModelSerializer):

    examples = ExamplesFilterSerializer(read_only=True, many=True)

    class Meta:
        model = ExamplesPhoto
        exclude = ("is_active",)


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        exclude = ("is_active", "for_main", "created_at", "updated_at")


# class BodyColourSerializer(serializers.ModelSerializer):

#     filling_scheme = SchemeFilterSerializer(read_only=True, many=True)

#     class Meta:
#         model = BodyColour
#         fields = ["id", "filling_scheme", "name", "image", "alt_text"]


# class DoorsSystemSerializer(serializers.ModelSerializer):

#     filling_scheme = SchemeFilterSerializer(read_only=True, many=True)

#     class Meta:
#         model = DoorsSystem
#         fields = ["id", "name", "position", "filling_scheme", "description"]


# class DoorsSystemFilterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DoorsSystem
#         fields = ["id", "name"]


# class DoorsProfilesSerializer(serializers.ModelSerializer):

#     doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

#     class Meta:
#         model = DoorsProfiles
#         fields = ["id", "name", "image", "doors_system", "description", "alt_text"]


# class DoorhandleSerializer(serializers.ModelSerializer):

#     doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

#     class Meta:
#         model = Doorhandle
#         fields = ["id", "name", "image", "doors_system", "description", "alt_text"]


# class DoorsMaterialsSerializer(serializers.ModelSerializer):

#     doors_system = DoorsSystemFilterSerializer(read_only=True, many=True)

#     class Meta:
#         model = DoorsMaterials
#         fields = ["id", "name", "image", "doors_system", "description", "alt_text"]
