from django.test import TestCase


# Create your tests here.
from LibraryProject.models import Book


class BasicTest(TestCase):

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

    def test_field(self):
        record = Book.objects.get(title="Gra o Tron")

        self.assertEqual(record, self.book)
