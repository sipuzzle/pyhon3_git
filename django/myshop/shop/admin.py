from django.contrib import admin
from .models import Category, Product
# Register your models here.


#定制商品种类注册
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']         #展示列表
    prepopulated_fields = {'slug': ('name',)}   #填入姓名后slug类自动填充
admin.site.register(Category, CategoryAdmin) #注册商品种类模块

#定制商品注册
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
