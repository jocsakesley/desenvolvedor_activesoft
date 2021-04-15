from django.db import models


class Album(models.Model):
    id = models.AutoField(db_column='AlbumId', primary_key=True)
    title = models.CharField(db_column='Title', max_length=160)
    artist = models.ForeignKey('chinook.Artist', db_column='ArtistId', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'albums'


class Artist(models.Model):
    id = models.AutoField(db_column='ArtistId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class Genre(models.Model):
    id = models.AutoField(db_column='GenreId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class MediaType(models.Model):
    id = models.AutoField(db_column='MediaTypeId', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_types'


class Track(models.Model):
    id = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')

    album = models.ForeignKey('chinook.Album', db_column='AlbumId', blank=True, null=True, on_delete=models.CASCADE)
    media_type = models.ForeignKey('chinook.MediaType', db_column='MediaTypeId', on_delete=models.CASCADE)

    genre = models.ForeignKey('chinook.Genre', db_column='GenreId', blank=True, null=True, on_delete=models.CASCADE,
                                related_name='tracks')

    composer = models.CharField(db_column='Composer', blank=True, null=True, max_length=220)
    milliseconds = models.IntegerField(db_column='Milliseconds')
    bytes = models.IntegerField(db_column='Bytes', blank=True, null=True)
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tracks'


class Customers(models.Model):
    id = models.AutoField(db_column='CustomerId', primary_key=True)
    first_name = models.CharField(db_column='FirstName', max_length=40)
    last_name = models.CharField(db_column='LastName', max_length=20)
    email = models.CharField(db_column='Email', max_length=60)

    company = models.CharField(db_column='Company', blank=True, null=True, max_length=80)
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=70)
    city = models.CharField(db_column='City', blank=True, null=True, max_length=40)
    state = models.CharField(db_column='State', blank=True, null=True, max_length=40)
    country = models.CharField(db_column='Country', blank=True, null=True, max_length=40)
    postal_code = models.CharField(db_column='PostalCode', blank=True, null=True, max_length=10)
    phone = models.CharField(db_column='Phone', blank=True, null=True, max_length=24)
    fax = models.CharField(db_column='Fax', blank=True, null=True, max_length=24)

    support_rep_id = models.IntegerField(db_column='SupportRepId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Playlist(models.Model):
    id = models.AutoField(db_column='PlaylistId', primary_key=True)
    name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)

    class Meta:
        managed = False
        db_table = 'playlists'
