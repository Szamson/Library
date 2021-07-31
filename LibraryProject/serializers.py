from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=50)
    publication_date = serializers.DateField()
    isbn = serializers.CharField(max_length=20)
    number_of_pages = serializers.IntegerField()
    cover = serializers.CharField(max_length=1000)
    language = serializers.CharField(max_length=20)


class BookFilterSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, allow_blank=True)
    author = serializers.CharField(max_length=100, allow_blank=True)
    language = serializers.CharField(max_length=20, allow_blank=True)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
