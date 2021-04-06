from django.shortcuts import render
from django.template import loader
from myapp import models
from django.http import HttpResponse

def product_page(request, handle):
    product = models.Product.objects.get(handle=handle)
    template = loader.get_template("product.html")
    context = {
        "product" : product
    }
    return HttpResponse(template.render(context, request))