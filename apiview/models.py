from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return f"Book: {self.book_name} Author: {self.author}"
