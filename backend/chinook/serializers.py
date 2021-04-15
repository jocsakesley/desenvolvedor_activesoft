from rest_framework import serializers
from chinook.models import Album, Artist, Genre, Playlist, Track


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        depth = 1


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'


class TrackSimplifiedSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(source='album.title', read_only=True)
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        total_seconds = obj.milliseconds/1000

        minutes = total_seconds // 60
        seconds = total_seconds - minutes*60

        return f'{minutes}min {seconds}s'

    class Meta:
        model = Track
        fields = ('id', 'name', 'composer', 'album_name', 'duration')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('name')
