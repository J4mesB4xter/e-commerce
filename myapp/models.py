
from django.db import models
from django_instant_rest.models import RestResource, RestClient
from mysite import settings

class Media(RestResource):
    filename = models.ImageField(upload_to='media')

    def download(self, url):
        """Store image locally if we have a URL"""

        if not self.filename:
            result = urllib.urlretrieve(url)
            self.filename.save(
                    os.path.basename(url),
                    File(open(result[0], 'rb'))
                    )
            self.save()

    class Meta:
        abstract = True

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

class CollectionMedia(Media):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='collection_media')

class ProductMedia(Media):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='product_media')

class VariantMedia(Media):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    filename = models.ImageField(upload_to='variant_media')