from django.urls import path
from .views import home, BooksGetViewTitle



urlpatterns = [
    path('', home, name='library-home'),
    path('books-title', BooksGetViewTitle.as_view())
]
