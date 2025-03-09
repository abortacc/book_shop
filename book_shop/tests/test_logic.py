from http import HTTPStatus

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

from catalog.models import Book, Author, Category
from accounts.models import Comment


User = get_user_model()


class TestCommentCreation(TestCase):

    COMMENT_TEXT = 'Какой-то комментарий'

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(title='Коты', slug='cats')
        cls.author = Author.objects.create(name='Автор')
        cls.book = Book.objects.create(
            title='Книга',
            category=cls.category,
            author=cls.author,
            price=599
        )
        cls.user = User.objects.create(username='myUser')
        cls.user_client = Client()
        cls.user_client.force_login(cls.user)
        cls.form_data = {'text': cls.COMMENT_TEXT}
        cls.comment_create_url = reverse('catalog:add_comment', args=(cls.book.id,))
        cls.comment_url = reverse('catalog:details', args=(cls.book.id,))

    def test_comment_creation(self):
        response = self.user_client.post(self.comment_create_url, data=self.form_data)
        self.assertRedirects(response, self.comment_url)
        comments_count = Comment.objects.count()
        self.assertEqual(comments_count, 1)
        comment = get_object_or_404(Comment, pk=self.book.id)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.text, self.COMMENT_TEXT)
