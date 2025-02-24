# Generated by Django 5.1.5 on 2025-02-20 10:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('bio', models.TextField(blank=True, verbose_name='Бигорафия')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_on_main', models.BooleanField(default=False, verbose_name='На главной')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Издательство')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'издателсьтва',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Тэг')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='В наличии')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('page_count', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество страниц')),
                ('description', models.TextField(blank=True, max_length=4096, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('book_format', models.CharField(choices=[('PB', 'Бумажная'), ('EB', 'Электронная'), ('AB', 'Аудиокнига')], max_length=2, verbose_name='Формат')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='books/covers/', verbose_name='Обложка книги')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='catalog.author', verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='Категория')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.publisher', verbose_name='Издательство')),
                ('tags', models.ManyToManyField(blank=True, related_name='books', to='catalog.tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]
