from django.urls import path
from .views import home, BooksGetViewTitle, addBook, importBook, AddBookView, DeleteBookView, searchRESTBook



urlpatterns = [
    path('', home, name='library-home'),
    path('add-book-manual', addBook),
    path('add-book-import', importBook),
    path('search-book-REST', searchRESTBook),
    path('books-title', BooksGetViewTitle.as_view()),
    path('books-add-view', AddBookView.as_view()),
    path('books-delete-view', DeleteBookView.as_view())

]
