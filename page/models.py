from django.db import models
from django.contrib.postgres.indexes import GinIndex


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    # class Meta:
    #     indexes = [
    #         GinIndex(fields=['name']),
    #         GinIndex(fields=['description']),
    #     ]
    class Meta:
        db_table = 'product_u3'

    def __str__(self):
        return self.name





