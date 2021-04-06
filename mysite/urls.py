from myapp.models import *
from django_instant_rest import patterns
from django.urls import path
from myapp import views

urlpatterns = [
    patterns.resource('collections.json', Collection),
    patterns.resource('products.json', Product),
    patterns.resource('variants.json', Variant),
    path('product/<handle>', views.product_page),
    ]