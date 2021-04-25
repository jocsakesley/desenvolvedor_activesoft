from rest_framework import serializers
from rest_framework import status
from chinook.models import Album, Artist, Genre, Playlist, Track, Customers, Invoices


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        depth = 1


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"


class TrackSimplifiedSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(source="album.title", read_only=True)
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        total_seconds = obj.milliseconds / 1000

        minutes = total_seconds // 60
        seconds = total_seconds - minutes * 60

        return f"{minutes}min {seconds}s"

    class Meta:
        model = Track
        fields = ("id", "name", "composer", "album_name", "duration")


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("name",)


class CustomerSimplifiedSerializer(serializers.ModelSerializer):
    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Nome não pode ter número")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Sobrenome não pode ter número")
        return value

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("E-mail deve ter @")
        return value

    class Meta:
        model = Customers
        fields = ("id", "first_name", "last_name", "email")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class CustomerInvoiceSerializer(serializers.Serializer):
    total__sum = serializers.DecimalField(max_digits=10, decimal_places=2)


class TotalPerCustomerSerializer(serializers.Serializer):
    def validate_customer_id(self, value):
        customers = [c.id for c in Customers.objects.all()]
        if value not in customers:
            raise serializers.ValidationError("ID de usuário não existe", code=status.HTTP_404_NOT_FOUND)
        return value

        if not isinstance(value, int):
            raise serializers.ValidationError("ID deve ser inteiro")
        return value

    def validate_year(self, value):
        if value not in range(1970,2100):
            raise serializers.ValidationError("Ano inválido")
        return value

        if not isinstance(value, int):
            raise serializers.ValidationError("Ano deve ser inteiro")
        return value

    customer_id = serializers.IntegerField()
    year = serializers.IntegerField()