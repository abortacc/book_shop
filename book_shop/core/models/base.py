from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StockModel(models.Model):
    stock = models.PositiveIntegerField(default=0)

    @property
    def is_avaible(self):
        return self.stock > 0

    class Meta:
        abstract = True
