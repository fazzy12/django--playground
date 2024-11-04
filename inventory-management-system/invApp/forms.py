from  django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            "product_id": "Product ID",
            "name": "Product Name",
            "sku": "Product SKU",
            "price": "Product Price",
            "quantity": "Product Quantity",
            "supplier": "Product Supplier",
        }
        widgets = {
            "product_id": forms.NumberInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "sku": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "supplier": forms.TextInput(attrs={"class": "form-control"}),
        }