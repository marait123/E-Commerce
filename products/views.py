from django.shortcuts import render
from .models import Product
from django.http import Http404, HttpRequest, JsonResponse
# Create your views here.
def products_featured(request):
    objects = Product.objects.get_featured_products()
    context = {'objects':objects}
    return render(request, 'products/list.html', context=context)

def product_list(request:HttpRequest):
    if request.method.lower() == 'get':
        args = request.GET
        page = args.get('page',1)
        print(page)
        objects = Product.objects.all()
        context = {'objects':objects}
        return render(request, 'products/list.html', context=context)
    else:
        return JsonResponse(status=405, data={
            'status':'fail',
            'message':'method not allowed'
        })
def product_detail_slug(request, slug):
    try:
        id = int(slug)
    except :
        id=None
    if id is None:
        product = Product.objects.get_product_by_slug(slug)    
    else:
        product = Product.objects.get_product_by_id(id)
    if not product:
        raise Http404("product doesn't exist")
    context = {'product':product}
    return render(request, 'products/detail.html', context = context)
def product_detail(request, id):
    product = Product.objects.get_product_by_id(id)
    if not product:
        raise Http404("product doesn't exist")
    context = {'product':product}
    return render(request, 'products/detail.html', context = context)