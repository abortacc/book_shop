from django.contrib import admin
from .models import Category, Tag, Author, Publisher, Book

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
