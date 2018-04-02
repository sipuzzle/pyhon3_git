from django.conf.urls import url,include
from . import views

#可以被页面调用的app名称
app_name='shop'

#顺序匹配，自动选择第一个匹配正则表达式成功的url

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),#正则表达式规范调用参数类型
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^cart/',include('cart.urls')),
]