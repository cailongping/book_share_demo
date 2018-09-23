# Generated by Django 2.1.1 on 2018-09-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_author',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_desc',
            field=models.TextField(verbose_name='简介'),
        ),
    ]
