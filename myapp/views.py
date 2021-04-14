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
        related_products = models.Product.objects.filter(title__startswith=title_prefix)
        template = loader.get_template("product.html")
        context = {
            "product" : product,
            "images" : images,
            "title_prefix" : title_prefix,
            "title_suffix" : title_suffix,
            "related_products" : related_products,
        }
        return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template("404.html")
        return HttpResponse(template.render({}, request))
        