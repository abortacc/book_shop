from django.db.models import Prefetch
from django.views.generic import ListView
from catalog.models import Book, Category


class IndexListView(ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'book_list_new'

    def get_queryset(self):
        return Book.objects.select_related(
            'category'
        ).prefetch_related(
            'tags'
        ).only(
            'id', 'title', 'category__title'
        ).filter(
            is_published=True,
            category__is_published=True
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related(
            Prefetch(
                'book_set',
                queryset=Book.objects.filter(
                    is_published=True
                ).order_by('-created_at')[:6],
                to_attr='prefatched_books'
            )
        ).filter(
            is_published=True,
            is_on_main=True
        )

        return context
