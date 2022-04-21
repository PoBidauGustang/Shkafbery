from django.urls import path

from . import views

urlpatterns = [
    path("step_one/", views.ClosetTypeListView.as_view()),
    path("step_two/", views.DimensionsListView.as_view()),
    path("step_three/", views.FillingSchemeListView.as_view()),
    path("step_fourth/", views.BodyColourListView.as_view()),
    # path("closet/<slug:slug>/", views.PostDetailView.as_view()),
]
