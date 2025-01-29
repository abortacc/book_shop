from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )

    class Meta:
        abstract = True


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано в'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменено в'
    )

    class Meta:
        abstract = True


class StockModel(models.Model):
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name='В наличии'
    )

    @property
    def is_avaible(self):
        return self.stock > 0

    class Meta:
        abstract = True
