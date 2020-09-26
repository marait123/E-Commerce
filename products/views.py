from django.shortcuts import render
from .models import Product
from django.http import Http404
# Create your views here.
def products_featured(request):
    objects = Product.objects.get_featured_products()
    context = {'objects':objects}
    return render(request, 'products/list.html', context=context)

def product_list(request):
    objects = Product.objects.all()
    print(objects)
    context = {'objects':objects}
    return render(request, 'products/list.html', context=context)
def product_detail(request, id):
    product = Product.objects.get_product_by_id(id)
    if not product:
        raise Http404("product doesn't exist")
    context = {'product':product}
    return render(request, 'products/detail.html', context = context)