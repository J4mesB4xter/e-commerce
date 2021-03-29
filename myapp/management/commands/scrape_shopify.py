
from django.core.management.base import BaseCommand
from myapp import models
import requests

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('store_url', nargs='+', type=str)

    def handle(self, *args, **options):
        store_url = options['store_url'].pop()

        # Collections
        # collections_url = f"{store_url}/collections.json?limit=250"
        # r = requests.get(collections_url)
        # collections = r.json()["collections"]

        # Products
        products_url = f"{store_url}/products.json?limit=250"
        r = requests.get(products_url)
        foreign_products = r.json()["products"]

        foreign_product = foreign_products.pop()
        
        native_product = {
            "title": None,
            "handle": None,
            "description": None,
            "collection": None,
        }
        
        
        native_product["handle"] = foreign_product["handle"]
        native_product["description"] = foreign_product["body_html"]
        native_product["title"] = foreign_product["title"]
        
        print(native_product)