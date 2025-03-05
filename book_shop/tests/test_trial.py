from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from catalog.models import Book, Author, Category


class TestBookCard(TestCase):
    TITLE = 'Название'
    DESCRIPTION = 'Описание'
    PAGE_COUNT = 200
    PRICE = 3499

    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Автор')
        cls.category = Category.objects.create(
            title='Категория',
            slug='category',
        )
        cls.book = Book.objects.create(
            title=cls.TITLE,
            description=cls.DESCRIPTION,
            author=cls.author,
            page_count=cls.PRICE,
            price=cls.PRICE,
            book_format='PB',
        )

    def test_book_detail(self):
        url = reverse('catalog:details', args=(self.book.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
