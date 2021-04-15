from django.shortcuts import render
from django.template import loader
from myapp import models
from django.http import HttpResponse

def product_page(request, handle):
    try:
        product = models.Product.objects.get(handle=handle)
        title_prefix = product.title.split(" - ")[0]
        title_suffix = product.title.split(" - ")[1]
        images = models.ProductMedia.objects.filter(product=product)
        variants = models.Variant.objects.filter(product=product)
        price = "$" + "{:.2f}".format(variants[0].price_in_cents/100)
        related_products = models.Product.objects.filter(title__startswith=title_prefix)
        template = loader.get_template("product.html")
        context = {
            "product" : product,
            "images" : images,
            "variants" : variants,
            "title_prefix" : title_prefix,
            "title_suffix" : title_suffix,
            "related_products" : related_products,
            "price" : price
        }
        return HttpResponse(template.render(context, request))
    except Exception as e:
        raise e
        template = loader.get_template("404.html")
        return HttpResponse(template.render({}, request))
        