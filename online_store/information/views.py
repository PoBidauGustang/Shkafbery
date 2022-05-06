from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutCompany, Examples, ExamplesPhoto, Faq
from .serializers import (
    AboutCompanySerializer,
    ExamplesPhotoSerializer,
    ExamplesSerializer,
    FaqSerializer,
)

# class DimensionsListView(APIView):DimensionsListView
#     """Displaying list of Closet Types"""

#     def get(self, request):
#         types = ClosetType.objects.filter(is_active=True)
#         serializer = ClosetTypeSerializer(types, many=True)
#         return Response(serializer.data)

# class AboutCompanyView(APIView):
#     """Displaying list dimensions"""

#     def get(self, request):
#         params = request.query_params.getlist("scheme")
#         dimensions = Dimensions.objects.filter(filling_scheme__in=params)
#         serializer = DimensionsSerializer(dimensions, many=True)
#         return Response(serializer.data)


class AboutCompanyView(APIView):
    """Displaying information about company"""

    def get(self, request):
        information = AboutCompany.objects.filter(is_active=True)
        serializer = AboutCompanySerializer(information, many=True)
        return Response(serializer.data)


class ExamplesListView(APIView):
    """Displaying list of work examples"""

    def get(self, request):
        examples = Examples.objects.filter(is_active=True, for_main=True)
        serializer = ExamplesSerializer(examples, many=True)
        return Response(serializer.data)


class ExamplesPhotoListView(APIView):
    """Displaying list of photos of work examples"""

    def get(self, request):
        photo = ExamplesPhoto.objects.filter(is_active=True)
        serializer = ExamplesPhotoSerializer(photo, many=True)
        return Response(serializer.data)


class FaqListView(APIView):
    """Displaying list of FAQ"""

    def get(self, request):
        question = Faq.objects.filter(is_active=True, for_main=True)
        serializer = FaqSerializer(question, many=True)
        return Response(serializer.data)
