from django.shortcuts import render
from django.template import loader
from myapp import models
from django.http import HttpResponse

def product_page(request):
    template = loader.get_template("product.html")
    context = {}
    return HttpResponse(template.render(context, request))