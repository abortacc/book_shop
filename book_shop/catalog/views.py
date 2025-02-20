from django.shortcuts import get_object_or_404
from django.db.models import Q, Prefetch, Count
from django.views.generic import ListView, DetailView
from .models import Book, Category


class CatalogListView(ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'book_list'
    paginate_by = 8

    def get_queryset(self):
        slug_name = self.kwargs.get('slug_name')
        if slug_name:
            return self.get_books_by_category(slug_name)
        else:
            return self.get_all_books()

    def get_books_by_category(self, slug_name):
        category = get_object_or_404(
            Category.objects.prefetch_related(
                Prefetch('book_set', queryset=Book.objects.filter(
                    is_published=True
                ).order_by('id', '-created_at'))
            ),
            slug=slug_name,
            is_published=True
        )
        self.category = category
        return category.book_set.all()

    def get_all_books(self):
        return Book.objects.select_related(
            'category'
        ).prefetch_related(
            'tags'
        ).filter(
            is_published=True,
            category__is_published=True
        ).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'category'):
            context['category'] = self.category
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

    def get_related_books(self, book):
        return Book.objects.filter(
            category=self.object.category,
            is_published=True
        ).exclude(
            id=self.object.id
        ).order_by(
            '-created_at'
        )[:6].select_related('category')

    def get_related_tag_books(self, book):
        return Book.objects.prefetch_related(
            'tags'
        ).filter(
            tags__in=self.object.tags.all()
        ).annotate(
            matching_tags_count=Count('tags')
        ).filter(
            matching_tags_count__gte=2
        ).exclude(
            id=self.object.id
        ).order_by(
            '-matching_tags_count',
            '-created_at'
        )[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_books'] = self.get_related_books(self.object)
        context['related_tag_books'] = self.get_related_tag_books(self.object)
        return context
