from django.shortcuts import render
from django.db.models import Q
from .models import Book


def catalog(request):
    template_name = 'catalog/catalog.html'
    books_list = Book.objects.all().filter(
        Q(is_published=True) & Q(category__is_published=True)
    )
    context = {
        'book_list': books_list
    }
    return render(request, template_name, context)
