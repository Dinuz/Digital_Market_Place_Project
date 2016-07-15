from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    description =  models.TextField(null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True, blank=True) # e.g. 100.02
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)  # e.g. 100.02

    def __str__(self):
        return self.title


