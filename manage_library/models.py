from django.db import models

from users.models import Users


class Book(models.Model):
    book_id = models.IntegerField(auto_created=True, primary_key=True)
    book_name = models.CharField(max_length=100)
    book_description = models.CharField(max_length=100, blank=True, null=True)
    is_available = models.BooleanField(default=True)


class BookStatus(models.Model):
    status_id = models.IntegerField(auto_created=True, primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_uid = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        models.UniqueConstraint(fields=["book_id", "user_uid"], name="unique_book_order")
