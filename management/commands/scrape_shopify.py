# Usage: python scripts/scrape_shopify.py https://somestore.com

import requests
import sys
from myapp import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Assuming the last command line argument was the url of a shopify store,
        # assigning it to a variable
        store_url = sys.argv.pop()

        print('here')
        print('here')
        print(store_url)
        exit()

        # Collections
        collections_url = f"{store_url}/collections.json?limit=250"
        r = requests.get(collections_url)
        collections = r.json()["collections"]

        # Products
        products_url = f"{store_url}/products.json?limit=250"
        r = requests.get(products_url)
        products = r.json()["products"]


        print(len(products))