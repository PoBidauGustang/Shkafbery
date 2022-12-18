from django.urls import path

from . import views

urlpatterns = [
    path("orders_list/", views.OrderListView.as_view()),
    # path("orders_list/", views.order_list_view),
    # path("order/<int:pk>/", views.ProductDetailView.as_view()),
    # path("order_item/<int:pk>/", views.ProductListView.as_view()),
    # path("products/", views.ProductListView.as_view()),
]
