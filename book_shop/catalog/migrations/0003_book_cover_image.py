# Generated by Django 5.1.5 on 2025-01-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_book_format_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/', verbose_name='Обложка книги'),
        ),
    ]
