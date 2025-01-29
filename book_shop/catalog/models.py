from django.db import models
from core.models.base import BaseModel, PublishedModel, StockModel


class Category(BaseModel, PublishedModel):
    pass


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
