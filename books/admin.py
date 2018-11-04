from django.contrib import admin

from books.models import Book, Publisher

admin.site.register(Book)
admin.site.register(Publisher)
