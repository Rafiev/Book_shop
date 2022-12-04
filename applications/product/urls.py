from django.urls import path

from applications.product.views import BookListApiView, BookRetrieveUpdateAPIView, BookCreateApiView, BookDestroyApiView

urlpatterns = [
    path('', BookListApiView.as_view()),
    path('post/', BookCreateApiView.as_view()),
    path('delete/<int:pk>/', BookDestroyApiView.as_view()),
    path('<int:pk>/', BookRetrieveUpdateAPIView.as_view())
]