from myapp.models import *
from django_instant_rest import patterns

urlpatterns = [
    patterns.resource('collections.json', Collection),
    patterns.resource('products.json', Product),
    patterns.resource('variants.json', Variant),
]