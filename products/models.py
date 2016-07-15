from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify


# Create your models here.


class Product(models.Model):
    slug = models.SlugField(blank=True)  # unique=True default='slug-field'
    title = models.CharField(max_length=30)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True, blank=True)  # e.g. 100.02
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)  # e.g. 100.02

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **Kwargs):
    #print(sender)
    #print(instance)
    if not instance.slug:
        instance.slug = slugify(instance.title) #'some-slug'

pre_save.connect(product_pre_save_receiver, sender=Product)

#def product_post_save_receiver(sender, instance, *args, **Kwargs):
#   # if instance.slug != slugify(instance.title):
#        instance.slug = slugify(instance.title)
#        instance.save()
#
#
#post_save.connect(product_post_save_receiver, sender=Product)