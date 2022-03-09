from rest_framework.response import Response
from rest_framework.views import APIView

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

from .serializers import ClosetTypeSerializer


class ClosetTypeListView(APIView):
    """Displaying list of Closet Types"""

    def get(self, request):
        posts = ClosetType.objects.filter(is_active=True)
        serializer = ClosetTypeSerializer(posts, many=True)
        return Response(serializer.data)
