from django import forms
from store.models import Product

class ProductForm(forms.ModelForm):
    # category = forms.Select()
    class Meta:
        model = Product
        fields = ('prod_name', 'category', 'description', 'image', 'price', 'in_stock')