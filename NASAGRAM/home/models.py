from django.db import models


class NasaData(models.Model):
    CAMERA_ID = models.IntegerField()
    CAMERA_NAME = models.CharField(max_length=100)
    EARTH_DATE = models.DateField()
    IMG_SRC = models.CharField(max_length=100)

    objects = models.Manager()


class NasaWallpaper(models.Model):
    TITLE = models.CharField(max_length=50)
    HDURL = models.CharField(max_length=100)
    IMG_SRC = models.CharField(max_length=100)
    DATE = models.DateField()

    objects = models.Manager()