from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from applications.product.models import Book
from applications.product.serializers import BookSerializer, BookListSerializer


class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookCreateApiView(CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDestroyApiView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.writer:
            return Response('You dont have permission to delete this book')
        self.perform_destroy(instance)
        return Response('Book successfully deleted', status=status.HTTP_204_NO_CONTENT)

