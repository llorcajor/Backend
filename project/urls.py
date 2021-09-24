from django.urls import path, include

from project import views

urlpatterns = [
    path("latest-projects/", views.LatestProjectsList.as_view()),
]
