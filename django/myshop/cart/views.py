from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
import logging

@require_POST

#购物车添加物品
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
#    logger = logging.getLogger("moshop.cart.cart_add.form")
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
#   logger.info(form)

    return redirect('cart:cart_detail')


#购物车删除物品
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

#购物车详情
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
      item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                  'update': True})
#   print (product_id)

    return render(request, 'cart/detail.html', {'cart': cart})