"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from products import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Product Views URL
    url(r'^detail/(?P<object_id>\d+)$', views.detail_view, name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)$', views.detail_slug_view, name='detail_view'),
    url(r'^detail/(?P<object_id>\d+)/edit/$', views.update_view, name='update_view'),
    url(r'^list/$', views.list_view, name='list_view'),
    url(r'^create/$', views.create_view, name='create_view'),
]
