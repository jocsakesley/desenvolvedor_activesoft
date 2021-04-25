from django.urls import path
from chinook.views import (
    AlbumListAPIView,
    PlaylistListAPIView,
    ReportDataAPIView,
    GenreListAPIView,
    TrackListAPIView,
    CustomerSimplifiedAPIView,
    TotalPerCustomerAPIView,
)

urlpatterns = [
    path("albums/", AlbumListAPIView.as_view()),
    path("genres/", GenreListAPIView.as_view()),
    path("tracks/", TrackListAPIView.as_view()),
    path("playlists/", PlaylistListAPIView.as_view()),
    path("report_data/", ReportDataAPIView.as_view()),
    path("customer_simplified/", CustomerSimplifiedAPIView.as_view()),
    path("total_per_customer/", TotalPerCustomerAPIView.as_view()),
]
