from django.db import models
from core.models.base import BaseModel, PublishedModel, StockModel


class Category(BaseModel, PublishedModel):
    title = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.title


class Tag(BaseModel):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Тэг'
    )

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'тэги'

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Бигорафия'
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.name


class Publisher(BaseModel):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Издательство'
    )

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'издателсьтва'

    def __str__(self):
        return self.name


class BookFormat(models.TextChoices):
    PAPERBOOK = 'PB', 'Бумажная'
    EBOOK = 'EB', 'Электронная'
    AUDIOBOOK = 'AB', 'Аудиокнига'


class Book(BaseModel, PublishedModel, StockModel):
    title = models.CharField(
        max_length=255, 
        verbose_name='Название'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Автор'
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Издательство'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='books',
        blank=True,
        verbose_name='Тэги'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book_format = models.CharField(max_length=2, choices=BookFormat.choices)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
