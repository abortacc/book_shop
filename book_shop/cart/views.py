from django.views.generic import TemplateView, View
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import JsonResponse


from .models import Cart, CartItem, Order
from catalog.models import Book
from core.models.mixins import AutoTemplateMixin


class CartTemplateView(AutoTemplateMixin, TemplateView):
    model = Cart
    template_name_suffix = '_main'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_cart()

        cart_items = cart.items.all()
        subtotal = sum(item.total_price for item in cart_items)
        total_quantity = sum(item.quantity for item in cart_items)

        context.update({
            'cart': cart,
            'cart_items': cart_items,
            'subtotal': subtotal,
            'total_quantity': total_quantity
        })
        return context

    def get_cart(self):
        if self.request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=self.request.user)
        else:
            session_key = self.request.session.session_key
            if not session_key:
                self.request.session.create()
                session_key = self.request.session.session_key
            cart, _ = Cart.objects.get_or_create(session_key=session_key)
        return cart


class AddToCartView(View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if not book.is_avaible:
            messages.error(request, f"Книга {book.title} недоступна")
            return redirect('catalog:book_detail', pk=book_id)

        cart = CartTemplateView.get_cart(self)
        quantity = int(request.POST.get('quantity', 1))

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        messages.success(request, f"Добавлено {book.title} в корзину")
        return redirect('cart:main')


class UpdateCartItemView(View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        action = request.POST.get('action')

        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        elif action == 'remove':
            cart_item.delete()
            messages.success(request, f"Книга {cart_item.book.title} удалена из корзины")
            return redirect('cart:main')

        cart_item.save()
        return redirect('cart:main')


class CheckoutView(AutoTemplateMixin, TemplateView):
    model = Cart
    template_name_suffix = '_checkout'

    def post(self, request):
        cart = self.get_cart()
        if not cart.items.exists():
            messages.error(request, "Корзина пуста")
            return redirect('cart:main')

        items = [{
            'book_id': item.book.id,
            'title': item.book.title,
            'quantity': item.quantity,
            'price': str(item.book.price),
            'total': str(item.total_price)
        } for item in cart.items.all()]

        order = Order.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            items=items,
            subtotal=sum(item.total_price for item in cart.items.all())
        )

        cart.items.all().delete()
        messages.success(request, f"Заказ #{order.id} успешно создан")
        return redirect('cart:success')


class SuccessView(AutoTemplateMixin, TemplateView):
    template_name_suffix = '_success'
