from django.db import models

# Create your models here.
class profile(models.Model):

    # database items
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()
    Image = models.ImageField()
    