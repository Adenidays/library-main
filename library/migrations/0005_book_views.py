# Generated by Django 4.2.4 on 2023-08-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
