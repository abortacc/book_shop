from django.db import models
from django.views.generic import ListView


from .mixins import AutoTemplateMixin


class IsOnMainModel(models.Model):
    is_on_main = models.BooleanField(
        default=False,
        verbose_name='На главной'
    )

    class Meta:
        abstract = True


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


class BaseListView(AutoTemplateMixin, ListView):
    paginate_by = 12
    context_object_name = 'objects'
    template_name_suffix = '_list'

    class Meta:
        abstract = True
