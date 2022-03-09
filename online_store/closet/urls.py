from django.urls import path

from . import views

urlpatterns = [
    path("step_one/", views.ClosetTypeListView.as_view()),
    # path("closet/<slug:slug>/", views.PostDetailView.as_view()),
]
