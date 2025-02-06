from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Prefetch, Count
from django.core.paginator import Paginator
from .models import Book, Category


def catalog(request, slug_name=None):
    template_name = 'catalog/catalog.html'

    if slug_name:
        category = get_object_or_404(
            Category.objects.prefetch_related(
                Prefetch('book_set', queryset=Book.objects.filter(
                    is_published=True
                ).order_by('id', '-created_at'))
            ),
            slug=slug_name,
            is_published=True
        )
        paginator = Paginator(category.book_set.all(), 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'category': category,
            'book_list': page_obj
        }
    else:
        books_list = Book.objects.all().filter(
            Q(is_published=True) & Q(category__is_published=True)
        ).order_by('id')
        paginator = Paginator(books_list, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'book_list': page_obj
        }
    return render(request, template_name, context)


def details(request, pk):
    template_name = 'catalog/details.html'
    book = get_object_or_404(
        Book.objects.all(),
        pk=pk
    )
    related_books = Book.objects.all().exclude(
        id=pk
    ).filter(
        category__title__exact=book.category.title,
        is_published=True
    ).order_by(
        '-created_at'
    )[:6]
    related_tag_books = Book.objects.all().prefetch_related(
        'tags'
    ).filter(
        tags__in=book.tags.all()
    ).annotate(
        matching_tags_count=Count('tags', filter=Q(tags__in=book.tags.all()))
    ).filter(
        matching_tags_count__gte=2
    ).exclude(
        id=pk
    )[:6]
    context = {
        "book": book,
        "related_books": related_books,
        "related_tag_books": related_tag_books
    }
    return render(request, template_name, context)
