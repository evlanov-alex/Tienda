from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
    #url(r'^search/$', views.index, name='index'),
]