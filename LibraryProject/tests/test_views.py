import unittest
import json
from django.test import RequestFactory
from ..models import Book
from ..views import home, importBook, addBook, searchRESTBook, BooksGetViewTitle, AddBookView, DeleteBookView


class UrlTests(unittest.TestCase):

    def setUp(self):
        self.book = Book()
        self.book.title = "Gra o Tron"
        self.book.author = "George R.R. Martin"
        self.book.language = "pl"
        self.book.number_of_pages = 831
        self.book.cover = "no"
        self.book.publication_date = "2011-04-21"
        self.book.isbn = "9873526201928"
        self.book.save()

    def test_homepage(self):
        factory = RequestFactory()
        request = factory.get('')

        response = home(request)
        self.assertEqual(200, response.status_code)

    def test_import_book(self):
        factory = RequestFactory()
        request = factory.get('/add-book-import/')

        response = importBook(request)
        self.assertEqual(200, response.status_code)

    def test_manual_add(self):
        factory = RequestFactory()
        request = factory.get('/add-book-manual/')

        response = addBook(request)
        self.assertEqual(200, response.status_code)

    def test_search_book(self):
        factory = RequestFactory()
        request = factory.get('/search-book-REST/')

        response = searchRESTBook(request)
        self.assertEqual(200, response.status_code)

    def test_REST_search(self):
        factory = RequestFactory()
        data = {
            "title": "Gra o Tron",
            "author": "George R.R. Martin",
            "language": "pl",
            "start_date": "2010-01-01",
            "end_date": "2021-01-01"
        }
        request = factory.post('/books-title/', json.dumps(data), content_type='application/json')
        view = BooksGetViewTitle.as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)

    def test_REST_add(self):
        factory = RequestFactory()
        data = {
            "title": self.book.title,
            "author": self.book.author,
            "language": self.book.language,
            "publication_date": self.book.publication_date,
            "number_of_pages": self.book.number_of_pages,
            "cover": self.book.cover,
            "isbn": self.book.isbn
        }
        request = factory.post('/books-add-view/', json.dumps(data), content_type='application/json')
        view = AddBookView.as_view()
        response = view(request)
        self.assertEqual(201, response.status_code)

    def test_REST_delete(self):
        factory = RequestFactory()
        data = {
            "title": self.book.title,
            "author": self.book.author,
            "language": self.book.language,
            "publication_date": self.book.publication_date,
            "number_of_pages": self.book.number_of_pages,
            "cover": self.book.cover,
            "isbn": self.book.isbn
        }
        request = factory.post('/books-delete-view/', json.dumps(data), content_type='application/json')
        view = DeleteBookView.as_view()
        response = view(request)
        self.assertEqual(200, response.status_code)
