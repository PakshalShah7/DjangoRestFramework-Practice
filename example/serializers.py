from rest_framework import serializers
from example.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ['id', 'artist_name']


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'album_name', 'artist']


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'song_name', 'artist', 'album']
