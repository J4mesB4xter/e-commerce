from django.shortcuts import render
from django.template import loader
from myapp import models
from django.http import HttpResponse

def product_page(request, handle):
    # try:
    product = models.Product.objects.get(handle=handle)
    image = models.ProductMedia.objects.select_related("product")[product.id-1].url
    template = loader.get_template("product.html")
    context = {
        "product" : product,
        "image" : image
    }
    return HttpResponse(template.render(context, request))
    # except:
    #     template = loader.get_template("404.html")
    #     return HttpResponse(template.render({}, request))
        