from django.urls import include, path

from django.urls import path, include

urlpatterns = [
    path('', include('chinook.urls')),
]
