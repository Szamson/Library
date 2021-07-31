from django.urls import path
from .views import home, BooksGetViewTitle, addBook



urlpatterns = [
    path('', home, name='library-home'),
    path('add-book-manual', addBook),
    path('books-title', BooksGetViewTitle.as_view())
]
