from django.shortcuts import render
from django.db.models import Q, Prefetch
from catalog.models import Book, Category


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

    categories = Category.objects.prefetch_related(
        Prefetch('book_set', queryset=Book.objects.filter(
            is_published=True).order_by('-created_at')
        )
    ).filter(
        is_published=True,
        is_on_main=True
    )
    context = {
        'book_list_new': book_list_new,
        'categories': categories
    }
    return render(request, template, context)
