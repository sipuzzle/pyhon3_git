from .cart import Cart

#定义cart上下文处理器
def cart(request):
    return {'cart': Cart(request)}