from django.views.generic import TemplateView


from catalog.models import Book
from .models import Order


class CartTemplateView(TemplateView):
    template_name = 'cart/cart.html'
