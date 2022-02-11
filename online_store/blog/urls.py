from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view()),
    path("post/<slug:slug>/", views.PostDetailView.as_view()),
]
