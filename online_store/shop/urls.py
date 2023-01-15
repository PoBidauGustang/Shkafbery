from django.urls import path

from . import views

urlpatterns = [
    path("product_categories/", views.CategoryListView.as_view()),
    path("popular_products/", views.PopularProductListView.as_view()),
    path("product/<int:pk>/", views.ProductDetailView.as_view()),
    path("products/<int:pk>/", views.ProductListView.as_view()),
    # path("products/", views.ProductListView.as_view()),
]
