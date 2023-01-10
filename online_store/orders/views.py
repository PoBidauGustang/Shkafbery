from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .models import (
    Order,
    OrderItem,
)
from .serializers import (
    OrderListSerializer,
    OrderSerializer,
    OrderItemsSerializer,
)


# class OrderListView(APIView):
#     """Displaying a list of orders"""

#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderListSerializer(orders, many=True)
#         return Response(serializer.data)


class OrderListView(generics.ListCreateAPIView):
    """Displaying a list of orders"""

    permission_classes = (IsAuthenticated,)

    orders = Order.objects.all()
    serializer_class = OrderListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # def get(self, request):
    #     orders = Order.objects.all()
    #     serializer = OrderListSerializer(orders, many=True)
    #     return Response(serializer.data)


@api_view(["GET", "POST"])
def order_list_view(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # order_data = JSONParser().parse(request)
        order_data = JSONParser().parse(request)

        serializer = OrderListSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderView(APIView):
#     """Displaying a list of orders"""

#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderListSerializer(orders, many=True)
#         return Response(serializer.data)


# class OrderItemView(APIView):
#     """Displaying a list of orders"""

#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderListSerializer(orders, many=True)
#         return Response(serializer.data)
