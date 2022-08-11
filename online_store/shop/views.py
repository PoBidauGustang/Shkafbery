from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
)
from .serializers import (
    CategoryListSerializer,
    ProductDetailSerializer,
    ProductListSerializer,
)


class CategoryListView(APIView):
    """Displaying a list of product categories"""

    def get(self, request):
        categories = Category.objects.filter(is_active=True)
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


# class CategoryListView(generics.ListAPIView):

#     queryset = Category.objects.filter(is_active=True)
#     serializer_class = CategoryListSerializer


class ProductListView(APIView):
    """Displaying list of product by category"""

    def get(self, request, pk):
        # params = request.query_params.getlist("category")
        # products = Product.objects.filter(category__in=params)
        products = Product.objects.filter(category=pk)
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Displaying product"""

    def get(self, request, pk):
        product = Product.objects.get(id=pk, is_active=True)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
