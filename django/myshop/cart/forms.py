from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

#购物车添加产品详情页
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                 coerce=int)
    update = forms.BooleanField(required=False,
                initial=False,
                widget=forms.HiddenInput)