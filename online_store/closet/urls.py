from django.urls import path

from . import views

urlpatterns = [
    path("step_one/", views.ClosetTypeListView.as_view()),
    path("step_two/", views.DimensionsListView.as_view()),
    path("step_three/", views.FillingSchemeListView.as_view()),
    path("step_fourth/", views.BodyColourListView.as_view()),
    path("step_fifth/", views.DoorsSystemListView.as_view()),
    path("step_sixth_profiles/", views.DoorsProfilesListView.as_view()),
    path("step_sixth_handle/", views.DoorhandleListView.as_view()),
    # path("closet/<slug:slug>/", views.PostDetailView.as_view()),
]
