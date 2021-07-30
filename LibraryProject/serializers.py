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


class BookTitleSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
