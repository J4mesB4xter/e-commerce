
from django.db import models
from django_instant_rest.models import RestResource, RestClient
from mysite import settings


class Collection(RestResource):
    title = models.CharField(max_length = 255)
    handle = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 2046)

class Product(RestResource):
    title = models.CharField(max_length = 255)
    handle = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 2046)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

class Variant(RestResource):
    title = models.CharField(max_length = 255)
    handle = models.CharField(max_length = 255, unique = True)
    price_in_cents = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class CollectionMedia(RestResource):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='collection_media')

class ProductMedia(RestResource):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='product_media')

class VariantMedia(RestResource):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='variant_media')