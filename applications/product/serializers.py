from rest_framework import serializers

from applications.product.models import Book


class BookSerializer(serializers.ModelSerializer):

    writer = serializers.EmailField(required=False)

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user)
        user = request.user
        book = Book.objects.create(writer=user, **validated_data)
        return book

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['writer', 'title', 'price']


