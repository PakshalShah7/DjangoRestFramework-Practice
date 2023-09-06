from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apiview.models import Author, Book
from apiview.serializers import AuthorSerializer, BookSerializer


class AuthorView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


class BookView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
