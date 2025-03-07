from django.test import TestCase
from django.urls import reverse

from catalog.models import Book, Author, Category


class TestCatalog(TestCase):

    PRICE = 3499

    @classmethod
    def setUpTestData(cls):
        cls.catalog_url = reverse('catalog:catalog_main')
        cls.math_category = Category.objects.create(
            title='Математика',
            slug='math'
        )
        cls.code_category = Category.objects.create(
            title='Программирование',
            slug='code'
        )
        cls.author = Author.objects.create(name='testUser')

        Book.objects.create(
            title='Название',
            price=cls.PRICE,
            author=cls.author,
            category=cls.code_category
        )

        same_category_book_card_list = [
            Book(
                title=f'Книга №{index}',
                price=cls.PRICE,
                author=cls.author,
                category=cls.math_category
            )
            for index in range(8)
        ]
        Book.objects.bulk_create(same_category_book_card_list)

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

    def test_catalog_by_category_books_count(self):
        url = reverse('catalog:catalog_category', args=(self.math_category.slug,))
        response = self.client.get(url)
        object_list = response.context['book_list']
        books_count = len(object_list)
        self.assertEqual(books_count, 8)

    def test_catalog_by_category_books(self):
        url = reverse('catalog:catalog_category', args=(self.math_category.slug,))
        response = self.client.get(url)
        object_list = response.context['book_list']
        self.assertTrue(
            all(book.category == self.math_category for book in object_list)
        )
