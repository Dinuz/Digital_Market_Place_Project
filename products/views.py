from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView


# Create your views here.

from marketplace.mixins import (
            MultiSlugMixin,
            SubmitBtnMixin,
            LoginRequiredMixin,
            )

from .models import Product
from .mixins import ProducManagerMixin
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





class ProductListView(ListView):

    model = Product
    #template_name = 'list_view.html'

    #def get_context_data(self, **kwargs):
    #    context = super(ProductListView, self).get_context_data(**kwargs)
    #    #context['now'] = timezone.now()
    #    print(context)
    #    context['queryset'] = self.get_queryset() #Product.objects.all()
    #    return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        #qs = qs.filter(title__icontains='sammmy')
        return qs


class ProductDetailView(MultiSlugMixin, DetailView):

    model = Product

    #def get_context_data(self, **kwargs):
    #    context = super(ProductDetailView, self).get_context_data(**kwargs)
    #    #context['now'] = timezone.now()
    #    #print(context)
    #    return context

    #def get_object(self, *args, **kwargs):
    #    slug = self.kwargs.get('slug')
    #    #print(slug)
    #    if slug is not None:
    #        try:
    #            obj = get_object_or_404(self.model, slug=slug)
    #        except self.model.MultipleObjectsReturned:
    #            obj = self.model.objects.filter(slug=slug).order_by('-title').first()
    #    else:
    #        obj = super(ProductDetailView, self).get_object(*args, **kwargs)
    #    # qs = qs.filter(title__icontains='sammmy')
    #    return obj


class ProductCreateView(LoginRequiredMixin, SubmitBtnMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'form.html'
    #fields = ['name']
    #success_url = '/products/create/'
    submit_btn = 'Add Product'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        return valid_data

    #def get_success_url(self):
    #   return reverse('product_list_view') #'/users/%s/' %(self.request.user)
#
    #def get_context_data(self, **kwargs):
    #    context = super(ProductCreateView, self).get_context_data(**kwargs)
    #    context['submit_btn'] = 'Add Product'
    #    #context['now'] = timezone.now()
    #    #print(context)
    #    return context


class ProductUpdateView(ProducManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
#class ProductUpdateView(ProducManagerMixin, LoginRequiredMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'form.html'
    #fields = ['name']
    #success_url = '/products/'
    submit_btn = 'Update Product'

    #def get_object(self, *args, **kwargs):
    #    user = self.request.user
    #    obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
    #    if obj.user == user or user in obj.managers.all():
    #        return obj
    #    else:
    #        raise Http404
    #    #return obj

    #def get_context_data(self, **kwargs):
    #    context = super(ProductUpdateView, self).get_context_data(**kwargs)
    #    context['submit_btn'] = 'Update Product'
    #    #context['now'] = timezone.now()
    #    #print(context)
    #    return context