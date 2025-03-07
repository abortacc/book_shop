from http import HTTPStatus

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from catalog.models import Book, Author, Category
from accounts.models import Comment


User = get_user_model()


class TestBookDetail(TestCase):
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

    def test_book_detail_url_access(self):
        url = reverse('catalog:details', args=(self.book.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestProfile(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testUser')
        cls.second_user = User.objects.create(username='testUser2')

    def test_profile_url_access(self):
        self.client.force_login(self.user)
        for arg in ((self.user.username,), (self.second_user.username,)):
            url = reverse('accounts:profile', args=arg)
            response = self.client.get(url)
            self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_edit_profile_url_access(self):
        self.client.force_login(self.user)
        url = reverse('accounts:edit_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestComments(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testUser')
        cls.second_user = User.objects.create(username='testUser2')
        cls.category = Category.objects.create(title='Коты', slug='cats')
        cls.author = Author.objects.create(name='Автор')
        cls.book = Book.objects.create(
            title='Книга',
            author=cls.author,
            price=499,
            category=cls.category
        )
        cls.comment = Comment.objects.create(
            user=cls.user,
            book=cls.book,
            text='Текст комментария'
        )

    def test_edit_delete_comment_access(self):
        user_statuses = (
            (self.user, HTTPStatus.OK),
            (self.second_user, HTTPStatus.FOUND)
        )
        for user, status in user_statuses:
            for operation in (
                'catalog:edit_comment',
                'catalog:delete_comment'
            ):
                with self.subTest(name=user):
                    self.client.force_login(user)
                    url = reverse(
                        operation,
                        args=(self.book.id, self.comment.id)
                    )
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, status)
