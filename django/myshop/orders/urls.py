from django.conf.urls import url
from . import views

app_name='order'

urlpatterns = [
        url(r'^create/$', views.order_create, name='order_create'),
]