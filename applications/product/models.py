from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descriptions = models.TextField(null=True, blank=True)
    date_of_created = models.DateField(auto_now_add=True)
    date_of_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title