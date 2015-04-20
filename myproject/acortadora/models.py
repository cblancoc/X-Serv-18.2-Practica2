from django.db import models

# Create your models here.


class Table(models.Model):
    real_url = models.CharField(max_length=64)
