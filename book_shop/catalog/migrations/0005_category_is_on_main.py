# Generated by Django 5.1.5 on 2025-02-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='На главной'),
        ),
    ]
