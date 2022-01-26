from django.urls import path

from . import views

urlpatterns = [
    path("productcategories/", views.CategoryListView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
]
