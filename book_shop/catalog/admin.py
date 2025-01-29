from django.contrib import admin
from .models import Category, Tag, Author, Publisher, Book


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'category',
        'author',
        'publisher',
        'book_format',
        'is_published',
        'stock',
        'created_at'
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'price',
        'is_published',
        'book_format',
        'stock'
    )
    search_fields = (
        'title',
        'author__name',
        'publisher__name'
    )
    list_filter = (
        'book_format',
        'category',
        'is_published'
    )
    ordering = (
        '-created_at',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'created_at'
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'title',
        'slug'
    )
    list_filter = (
        'is_published',
    )
    ordering = (
        'title',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'birth_date',
        'created_at'
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'birth_date',
    )
    ordering = (
        'name',
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at'
    )
    search_fields = (
        'name',
    )
    ordering = (
        'name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
