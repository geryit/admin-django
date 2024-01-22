from django.db import models

# Create your models here.
from django.db import models


class Work(models.Model):
    year = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    long_desc = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)