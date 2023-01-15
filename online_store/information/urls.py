from django.urls import path

from . import views

urlpatterns = [
    path("about_company/", views.AboutCompanyView.as_view()),
    path("work_examples/", views.ExamplesListView.as_view()),
    path("examples_photos/", views.ExamplesPhotoListView.as_view()),
    path("FAQ/", views.FaqListView.as_view()),
    path("main_page_header/", views.MainPageHeaderView.as_view()),
]
