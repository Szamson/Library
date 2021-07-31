from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    number_of_pages = models.IntegerField()
    cover = models.CharField(max_length=1000)
    language = models.CharField(max_length=20)
