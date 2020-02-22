from django.db import models

class Cars(models.Model):
    maker = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    description = models.TextField()
    color = models.CharField(max_length=255, null=False)
    doors = models.IntegerField(default=0)
    lot = models.IntegerField(default=0)
# Create your models here.
