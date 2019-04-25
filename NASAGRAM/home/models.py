from django.db import models

class NasaData(models.Model):
    CAMERA_ID = models.IntegerField()
    CAMERA_NAME = models.CharField(max_length=100)
    EARTH_DATE = models.CharField(max_length=20)
    IMG_SRC = models.CharField(max_length=100)

    objects = models.Manager()
