from django.views.generic import TemplateView, RedirectView
from django.shortcuts import get_list_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail


from catalog.models import Book
from .models import Order
from core.models.mixins import AutoTemplateMixin


class CartTemplateView(AutoTemplateMixin, TemplateView):
    template_name_suffix = '_main'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', [])

        cart_items = []
        subtotal = 0
        total_quantity = 0

        for item in cart:
            product = get_list_or_404(Book, id=item['product_id'])
            total_quantity += item['quantity']
            item_total = product.price * item['quantity']
            cart_items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'item_total': item_total
            })

            subtotal += item_total

        context['cart_items'] = cart_items
        context['subtotal'] = subtotal
        context['item_quantity'] = total_quantity
        return context
