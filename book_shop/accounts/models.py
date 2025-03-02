from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from core.models.base import BaseModel, PublishedModel
from catalog.models import Book


class CustomUser(AbstractUser):
    rating = models.FloatField(
        default=0.0,
        blank=True,
        verbose_name='Рейтинг'
    )
    avatar = models.ImageField(
        upload_to='users/avatars/',
        default='users/avatars/def_avatar.png',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True,
        verbose_name='Подписчики'
    )
    wishlist = models.ManyToManyField(
        Book,
        blank=True,
        related_name='desired_by',
        verbose_name='Желаемое'
    )

    def __str__(self):
        return self.username


User = get_user_model()


class Comment(BaseModel, PublishedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пользователь'
    )
    book = models.ForeignKey(
        'catalog.Book',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='Книга'
    )
    text = models.TextField(max_length=2056, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'Комментарий пользователя {self.user} №{self.id}'


class Award(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='awards',
        verbose_name='Пользователь'
    )
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(
        blank=True,
        max_length=256,
        verbose_name='Описание'
    )
    received_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Получил'
    )

    class Meta:
        verbose_name = 'Награды'
        verbose_name_plural = 'награды'

    def __str__(self):
        return self.name


class Order(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Пользователь'
    )
    books = models.ManyToManyField(
        Book,
        verbose_name='Заказы',
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ {self.user.username} №{self.id}'


class Library(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='library',
        verbose_name='Пользователь'
    )
    books = models.ManyToManyField(
        Book,
        related_name='purchased_by',
        verbose_name='Книги'
    )

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'библиотеки'

    def __str__(self):
        return f'Библиотека пользователя {self.user.username}'
