from django.db import models


class Package(models.Model):
    Destination = models.CharField(max_length=250)
    Price = models.IntegerField(max_length=250)



