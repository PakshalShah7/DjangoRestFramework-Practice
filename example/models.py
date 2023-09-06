from django.db import models


class Artist(models.Model):
    artist_name = models.CharField(max_length=30)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists')

    def __str__(self):
        return f"Album: {self.album_name} Artist: {self.artist}"


class Song(models.Model):
    song_name = models.CharField(max_length=30)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='song_artists')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"Song: {self.song_name} Artist: {self.artist} Album: {self.album}"
