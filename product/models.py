from django.db import models
from account.models import BookSeller
# Create your models here.

class Book(models.Model):
    book_owner = models.ForeignKey(BookSeller, related_name='book_seller', on_delete=models.CASCADE)
    book_category = models.CharField(max_length=200) 
    book_title = models.CharField(max_length=200)
    book_price = models.IntegerField()
    book_edition = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_old = models.IntegerField()
    book_page = models.IntegerField()
    book_description = models.TextField(max_length=200)
    book_image_1 = models.ImageField(upload_to='book/book_photos/%Y/%m/%d', blank=True)
    book_image_2 = models.ImageField(upload_to='book/book_photos/%Y/%m/%d', blank=True)
    book_image_3 = models.ImageField(upload_to='book/book_photos/%Y/%m/%d', blank=True)
    book_image_4 = models.ImageField(upload_to='book/book_photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.book_title