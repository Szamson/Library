import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import BookSerializer, BookFilterSerializer

# Create your views here.
from LibraryProject.models import Book


def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "homepage.html", context)


class BooksGetViewTitle(APIView):
    serializer_class = BookFilterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid()
        if valid:

            queryset = None

            if len(serializer.data.get('title')) != 0:
                title = serializer.data.get('title')
            else:
                title = ""
            if len(serializer.data.get('author')) != 0:
                author = serializer.data.get('author')
            else:
                author = ""
            if len(serializer.data.get('language')) != 0:
                language = serializer.data.get('language')
            else:
                language = ""
            if len(serializer.data.get('end_date')) != 0:
                end_date = datetime.date.today()
            else:
                end_date = serializer.data.get('end_date')
            if len(serializer.data.get('start_date')) != 0:
                start_date = datetime.date(1000, 1, 1)
            else:
                start_date = serializer.data.get('start_date')

            queryset = Book.objects.get(title__contains=title, author__contains=author, language__contains=language,
                                        publication_date__range=[start_date, end_date])

            if queryset is not None:
                return Response(BookSerializer(queryset).data, status=status.HTTP_200_OK)
            else:
                return Response({'Not Found': 'Invalid title...'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class AddBookView(APIView):

    serializer_class = BookSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            title = serializer.data.get('title')
            author = serializer.data.get('author')
            publication_date = serializer.data.get('publication_date')
            isbn = serializer.data.get('isbn')
            number_of_pages = serializer.data.get('number_of_pages')
            cover = serializer.data.get('cover')
            language = serializer.data.get('language')

            queryset = Book.objects.get(title=title, author=author, language=language,
                                        publication_date=publication_date, isbn=isbn, number_of_pages=number_of_pages,
                                        cover=cover)
            if len(queryset) > 0:
                return Response({'Bad Request': 'Book already exists...'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                book = Book(title=title, author=author, publication_date=publication_date, isbn=isbn,
                            number_of_pages=number_of_pages, cover=cover, language=language)
                book.save()
                return Response({'Success': 'Book added...'}, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
