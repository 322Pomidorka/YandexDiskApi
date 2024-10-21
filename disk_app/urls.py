from django.urls import path

from .views import file_list_view

urlpatterns = [
    path("", file_list_view, name="file_list"),
]