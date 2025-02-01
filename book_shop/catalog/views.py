from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Prefetch
from .models import Book, Category


def catalog(request, slug_name=None):
    template_name = 'catalog/catalog.html'

    if slug_name:
        category = get_object_or_404(
            Category.objects.prefetch_related(
                Prefetch('book_set', queryset=Book.objects.filter(
                    is_published=True
                ).order_by('-created_at'))
            ),
            slug=slug_name,
            is_published=True
        )
        context = {
            'category': category,
            'book_list': category.book_set.all()
        }
    else:
        books_list = Book.objects.all().filter(
            Q(is_published=True) & Q(category__is_published=True)
        )
        context = {
            'book_list': books_list
        }
    return render(request, template_name, context)
