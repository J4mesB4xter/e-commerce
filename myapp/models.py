from django.core.files import File
from django.db import models
from django_instant_rest.models import RestResource, RestClient
from mysite import settings
from urllib.request import urlretrieve
import os

class Collection(RestResource):
    title = models.CharField(max_length = 255)
    handle = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 2046)

class Product(RestResource):
    title = models.CharField(max_length = 255)
    handle = models.CharField(max_length = 255, unique = True)
    description = models.CharField(max_length = 2046)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

class Variant(RestResource):
    title = models.CharField(max_length = 255)
    price_in_cents = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class CollectionMedia(RestResource):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    url = models.CharField(max_length = 1023)

class ProductMedia(RestResource):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length = 1023)
    
class VariantMedia(RestResource):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    url = models.CharField(max_length = 1023)