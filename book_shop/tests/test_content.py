from django.test import TestCase
from django.urls import reverse

from catalog.models import Book, Author, Category


class TestCatalog(TestCase):

    PRICE = 3499

    @classmethod
    def setUpTestData(cls):
        cls.catalog_url = reverse('catalog:catalog_main')
        cls.category = Category.objects.create(
            title='Математика',
            slug='math'
        )
        cls.author = Author.objects.create(name='testUser')
        book_card_list = [
            Book(
                title=f'Книга №{index}',
                price=cls.PRICE,
                author=cls.author,
                category=cls.category
            )
            for index in range(20)
        ]
        Book.objects.bulk_create(book_card_list)

    def test_catalog_books_count(self):
        response = self.client.get(self.catalog_url)
        object_list = response.context['book_list']
        books_count = object_list.count()
        self.assertEqual(books_count, 8)

    def test_catalog_books_order(self):
        response = self.client.get(self.catalog_url)
        object_list = response.context['book_list']
        books = list(object_list)
        oredered_books = sorted(books, key=lambda book: book.id)
        self.assertEqual(books, oredered_books)
