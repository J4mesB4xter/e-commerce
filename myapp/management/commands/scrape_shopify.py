
from django.core.management.base import BaseCommand
from myapp import models
import requests

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('store_url', nargs='+', type=str)

    def handle(self, *args, **options):
        store_url = options['store_url'].pop()
        products_url = f"{store_url}/products.json?limit=250"
        r = requests.get(products_url)
        foreign_products = r.json()["products"]
        
        for foreign_product in foreign_products:
            native_product = models.Product.objects.create(
                title = foreign_product["title"],
                handle = foreign_product["handle"],
                description = foreign_product["body_html"],
                collection = None,
            )

            native_variants = []
            for variant in foreign_product["variants"]:
                native_variant = models.Variant.objects.create(
                    title = variant["title"],
                    price_in_cents = int(float(variant["price"])* 100),
                    product = native_product,
                )
                for image in foreign_product["images"]:
                    native_product_media = models.ProductMedia.objects.create(
                        product = native_product,
                        url = image["src"]
                    )
            print(native_product.handle)