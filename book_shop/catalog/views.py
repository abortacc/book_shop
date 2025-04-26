from django.shortcuts import get_object_or_404, redirect
from django.db.models import Prefetch, Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from .models import Book, Category, Tag
from accounts.models import Comment
from .forms import CommentForm
from core.models.base import BaseListView


class CatalogListView(BaseListView):
    model = Book
    context_object_name = 'book_list'

    def get_queryset(self):
        slug_name = self.kwargs.get('slug_name')
        if slug_name:
            queryset = self.get_books_by_category(slug_name)
        else:
            queryset = self.get_all_books()

        tag_slugs = self.request.GET.getlist('tag')
        if tag_slugs:
            queryset = queryset.filter(tags__slug__in=tag_slugs).distinct()

        return queryset

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
        ).order_by('-created_at')

    def get_all_tags(self):
        return Tag.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.get_all_tags()
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
            '?'
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
        context['comments'] = self.object.comments.all()
        context['form'] = CommentForm()
        return context


class CommentMixin(LoginRequiredMixin):
    model = Comment
    template_name = 'catalog/comment.html'
    pk_url_kwarg = 'comment_id'

    def dispatch(self, request, *args, **kwargs):
        comment = get_object_or_404(
            Comment,
            pk=kwargs['comment_id']
        )
        if comment.user != request.user:
            return redirect('catalog:details', pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('catalog:details', kwargs={'pk': self.kwargs['pk']})


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'catalog/comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:details', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(CommentMixin, UpdateView):
    form_class = CommentForm


class CommentDeleteView(CommentMixin, DeleteView):
    pass
