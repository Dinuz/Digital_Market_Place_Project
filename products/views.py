from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product
from .forms import ProductAddForm, ProductModelForm


def create_view(request):
    #print(request.POST)
    # FORMS
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()


    #form = ProductAddForm(request.POST or None)
    #if request.method == 'POST':
    #    print(request.POST)
    #if form.is_valid():
    #    data = form.cleaned_data
    #    title = data.get('title')
    #    description = data.get('description')
    #    price = data.get('price')
#
    #    new_object = Product.objects.create(title=title, description=description, price=price)

        #new_object = Product()
        #new_object.title = title
        #new_object.description = description
        #new_object.price = price
        #new_object.save()

        #print(request.POST)

    #template = 'create_view.html'
    template = 'form.html'
    context = {
        'form': form,
        'submit_btn': 'Create Product',
    }

    return render(request, template, context)


def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        #instance.sale_price = instance.price
        instance.save()
    #template = 'update_view.html'
    template = 'form.html'
    context = {
        'product': product,
        'form': form,
        'submit_btn': 'Update Product',
    }

    return render(request, template, context)


def detail_slug_view(request, slug=None):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by('-title').first()
    #print(slug)
    #product = 1
    template = 'detail_view.html'
    context = {
        'product': product
    }

    return render(request, template, context)


def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = 'detail_view.html'
    context = {
        'product': product
    }

    return render(request, template, context)

    #try:
    #    product = get_object_or_404(Product, id=object_id)
    #except ValueError:
    #    raise Http404
    #
    #if object_id is not None:
    #    product = get_object_or_404(Product, id=object_id)
    #    #product = Product.objects.get(id=object_id)
    #    #try:
    #    #    product = Product.objects.get(id=object_id)
    #    #except Product.DoesNotExist:
    #    #    product = None
    #    template = 'detail_view.html'
    #    context = {
    #        'product': product
    #    }
#
    #    return render(request, template, context)
    #else:
    #    raise Http404



def list_view(request):
    print(request)

    queryset = Product.objects.all()
    template = 'list_view.html'
    context = {
        'queryset': queryset
    }
    return render(request, template, context)