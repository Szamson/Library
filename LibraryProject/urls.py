from django.urls import path
from .views import home, BooksGetView



urlpatterns = [
    path('', home, name='library-home'),
    path('books-title', BooksGetView.as_view())
]
