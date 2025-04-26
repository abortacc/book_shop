from django.db import models
from django.contrib.auth import get_user_model


from core.models.base import BaseModel
from catalog.models import Book


User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Пользователь',
        null=True,
        blank=True
    )
    session_key = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        verbose_name='Ключ сессии'
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f'Корзина {self.user.username}'


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Корзина'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Книга'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'элементы корзины'

    def __str__(self):
        return f'{self.book.title} x {self.quantity}'

    @property
    def total_price(self):
        return self.book.price * self.quantity


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
