from rest_framework import serializers
from apiview.models import Author, Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'book_name', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    authors = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'author_name', 'authors']

    def create(self, validated_data):
        books_data = validated_data.pop('authors')
        author = Author.objects.create(**validated_data)
        Book.objects.create(author=author, **books_data)
        return author
