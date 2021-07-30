from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=20, null=True)
    number_of_pages = models.IntegerField(null=True)
    cover = models.CharField(null=True, max_length=1000) #As Base64
    language = models.CharField(max_length=20, null=True)
