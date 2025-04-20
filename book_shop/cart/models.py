from django.db import models


from core.models.base import BaseModel


class Order(BaseModel):
    name = models.CharField(max_length=128, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    items = models.JSONField(verbose_name='Товары заказа')
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ от {self.name}'
