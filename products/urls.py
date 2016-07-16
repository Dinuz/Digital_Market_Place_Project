from django.conf.urls import url

#from . import views

from .views import (
        ProductListView,
        ProductDetailView,
        ProductCreateView,
        ProductUpdateView,
        )

#app_name = 'products'

urlpatterns = [

    # Product Views URL
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)$', ProductDetailView.as_view(), name='detail_slug'),
    url(r'^create/$', ProductCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='update_slug'),
]