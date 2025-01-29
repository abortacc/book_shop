from django.shortcuts import render
from django.db.models import Q
from catalog.models import Book


def index(request):
    template = 'homepage/index.html'
    book_list_new = Book.objects.select_related(
        'author', 'category'
    ).prefetch_related(
        'tags'
    ).filter(
        (Q(is_published=True)
        & Q(category__is_published=True))
    ).order_by(
        '-created_at'
    )[:3]
    context = {
        'book_list_new': book_list_new
    }
    return render(request, template, context)
