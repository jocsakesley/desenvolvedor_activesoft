from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from chinook.serializers import (
    AlbumSerializer,
    GenreSerializer,
    PlaylistSerializer,
    TrackSimplifiedSerializer,
    TrackSerializer,
    CustomerSimplifiedSerializer,
    CustomerSerializer,
    TotalPerCustomerSerializer,
    CustomerInvoiceSerializer,
)
from django.db.models import Sum, F, FloatField
from chinook.models import Album, Genre, Playlist, Track, Customers, Invoices

from core.utils import sql_fetch_all


class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.select_related('artist')
    serializer_class = AlbumSerializer


class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.prefetch_related("tracks")
    serializer_class = GenreSerializer


class PlaylistListAPIView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class TrackListAPIView(ListAPIView):
    queryset = Track.objects.select_related(
        "album"
    )
    serializer_class = TrackSimplifiedSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "name", "composer"]


class ReportDataAPIView(APIView):
    def get(self, request, *args, **kwargs):

        dado = sql_fetch_all(
            """
                SELECT *, customers.[FirstName], customers.[LastName], 
                    customers.[FirstName] || ' ' || customers.[LastName] as FullName
                FROM customers
                LEFT JOIN employees ON employees.[EmployeeId] = customers.[SupportRepId]
                ORDER BY customers.[CustomerId]
            """
        )

        return Response(dado)


class CustomerSimplifiedAPIView(APIView):
    def get(self, request, *args, **kwargs):
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSimplifiedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TotalPerCustomerAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TotalPerCustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer_invoices = Invoices.objects.filter(
                customerid=serializer.data.get('customer_id')
                ).filter(
                    invoicedate__year=serializer.data.get('year')
                ).aggregate(Sum(F("total")))
        
            invoices_serializer = CustomerInvoiceSerializer(customer_invoices)
            
            return Response(invoices_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
