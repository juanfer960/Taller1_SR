from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.pastword

class Registry(models.Model):
    userId = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    musicbrainzArtistId = models.CharField(max_length=100, null=True, blank=True)
    artistName = models.CharField(max_length=100, null=True, blank=True)
    musicbrainzTrackId = models.CharField(max_length=100,null=True, blank=True)
    trackName = models.CharField(max_length=100, null=True, blank=True)


class PREDICTION_CHART(models.Model):
    userId = models.CharField(max_length=100, null=True, blank=True)
    artistId = models.CharField(max_length=200, null=True, blank=True)
    prediction = models.CharField(max_length=200, null=True, blank=True)
