from django.urls import path
from .views import home, BooksGetViewTitle, addBook, importBook, AddBookView



urlpatterns = [
    path('', home, name='library-home'),
    path('add-book-manual', addBook),
    path('add-book-import', importBook),
    path('books-title', BooksGetViewTitle.as_view()),
    path('books-add-view', AddBookView.as_view())

]
