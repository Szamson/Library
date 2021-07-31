from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'publication_date',
            'isbn',
            'number_of_pages',
            'cover',
            'language'
        )


class BookFilterSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, allow_blank=True)
    author = serializers.CharField(max_length=100, allow_blank=True)
    language = serializers.CharField(max_length=20, allow_blank=True)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
