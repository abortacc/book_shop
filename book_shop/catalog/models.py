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
    pass


class Format(BaseModel):
    pass


class Book(BaseModel, PublishedModel, StockModel):
    pass
