from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class RegisterApiView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Your are successfully registered, we send a message to your email for activate user!')


class ActivationApiView(APIView):

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Successfully activate.', status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response('Incorrect code!', status=status.HTTP_400_BAD_REQUEST)

