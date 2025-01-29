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
    pass


class Author(BaseModel):
    pass


class Publisher(BaseModel):
    pass


class Format(BaseModel):
    pass


class Book(BaseModel, PublishedModel, StockModel):
    pass
