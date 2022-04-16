from rest_framework.response import Response
from rest_framework.views import APIView
# from django_filters import rest_framework as filters
# from rest_framework import generics

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
from .serializers import (
    ClosetTypeSerializer,
    DimensionsSerializer,
    FillingSchemeSerializer,
)


class ClosetTypeListView(APIView):
    """Displaying list of Closet Types"""

    def get(self, request):
        types = ClosetType.objects.filter(is_active=True)
        serializer = ClosetTypeSerializer(types, many=True)
        return Response(serializer.data)


# class ClosetTypeListView(generics.ListAPIView):
#     """Displaying list of Closet Types"""

#     # def get(self, request):
#     queryset = ClosetType.objects.filter(is_active=True)
#     serializer = ClosetTypeSerializer(queryset, many=True)
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_fields = ('type')


class FillingSchemeListView(APIView):
    """Displaying list of Filling Schemes"""

    def get(self, request):
        schemes = FillingScheme.objects.filter(is_active=True)
        serializer = FillingSchemeSerializer(schemes, many=True)
        return Response(serializer.data)


class DimensionsListView(APIView):
    """Displaying list dimensions"""

    def get(self, request):
        params = request.query_params.getlist("scheme")
        dimensions = Dimensions.objects.filter(filling_scheme__in=params)
        serializer = DimensionsSerializer(dimensions, many=True)
        return Response(serializer.data)
