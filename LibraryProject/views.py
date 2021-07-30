from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import BookSerializer, BookTitleSerializer

# Create your views here.
from LibraryProject.models import Book


def home(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "homepage.html", context)


class BooksGetView(APIView):
    serializer_class = BookTitleSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        v = serializer.is_valid()

        if v:
            title = serializer.data.get('title')
            queryset = Book.objects.get(title__contains=title)
            if queryset is not None:
                return Response(BookSerializer(queryset).data, status=status.HTTP_200_OK)
            else:
                return Response({'Not Found': 'Invalid title...'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
