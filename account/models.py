from django.db import models

# Create your models here.

class BookSeller(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=100)
    user_photo = models.ImageField(upload_to='book/seller_photos/%Y/%m/%d/', blank=True)
    user_address = models.CharField(max_length=300)
    user_state = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name