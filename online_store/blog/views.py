from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostListView(APIView):
    """Displaying list of posts"""

    def get(self, request):
        posts = Post.objects.filter(status="published")
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    """Displaying post"""

    def get(self, request, slug):
        post = Post.objects.get(slug=slug, status="published")
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostListCarouselView(APIView):
    """Displaying list of news for carousel"""

    def get(self, request):
        posts = Post.objects.filter(news_carousel=True, status="published")
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
