from django.urls import path

from . import views

urlpatterns = [
    path("product_categories/", views.CategoryListView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
]
